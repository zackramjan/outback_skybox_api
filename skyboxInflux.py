#!/usr/bin/env python3
import json
import sys
import time
import traceback
from datetime import date, datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import SkyboxAPI

def logIt(msg):
    print(str(datetime.now()) + ": " + msg, file=sys.stderr, flush=True)

def readConfig():
   f = open('config.json', "r") 
   config = json.load(f)
   token = config["token"]
   org = config["org"]
   bucket = config["bucket"]
   url = config["url"]
   skyboxurl = config["skyboxurl"]
   sleeptime = int(config["sleeptime"])
   f.close() 
   return config["token"],config["org"],config["bucket"],config["url"],config["skyboxurl"],int(config["sleeptime"])


#this is an example usage of the SkyboxAPI to retrieve the various metrics, notifications and errors and send them to the influxDB cloud account for viewing and plotting
def main(argv=None): 
    #we will loop forever, if we encounter an error we will restart here and try again
    while True:
        try:
            #lets read our config.json file which has our secret keys for influx etc along with other settings
            f = open('config.json', "r") 
            config = json.load(f)
            token = config["token"]
            org = config["org"]
            bucket = config["bucket"]
            url = config["url"]
            skyboxurl = config["skyboxurl"]
            sleeptime = int(config["sleeptime"])
            
            #connect to influxDB with your key and url
            client = InfluxDBClient(url=url, token=token, verify_ssl=False)
            
            #create the skyboxAPI object
            s = SkyboxAPI.SkyboxAPI()
            print("logging into " +  skyboxurl)
            
            #login to skybox
            loginStatus = s.login(skyboxurl) 
            #loop forever here, this is the main loop
            while True:
                try:
                    #get all the metrics
                    status = s.getStatus()
                    
                    #get the last alert
                    alert =  s.getAlerts()[0]
                    
                    #get the last warning
                    notifcation =  s.getNotifications()[0]
                    
                    #add the last alert and warning to the upload string for influxdb
                    infuxInsertString = "skybox lastNotice=\"" + str(datetime.fromtimestamp(int(notifcation["Timestamp"])/1000))  + " " + notifcation["Message"] + "\","
                    infuxInsertString += "lastAlert=\"" +  str(datetime.fromtimestamp(int(alert["Timestamp"])/1000))  + " " + alert["Message"] + "\","
                    statusMsg = "PV_WATTS=" + str(float(status["pv_output_power_dc"])) + "\tPV_VOLTS=" + str(float(status["pv_pmb_voltage"])) + "\tGRID_WATTS=" + str(float(status["grid_realtime_wattage_sum"])) + "\tBATT_WATTS=" + str(float(status["battery_watts"])) + "\tBATT_VOLTS=" + str(float(status["battery_voltage"])) + "\tBATT_SOC=" + str(float(status["battery_state_of_charge"]))
                    
                    #add the metrics to the upload string for influxdb, we can ignore metrics that end with _property
                    for e in sorted(status):
                        if not e.endswith("_property"):
                            try:
                                val = float(status[e])
                                infuxInsertString += e + "=" +  status[e].lower() + ","
                            except:
                                pass
                                
                except:
                    logIt("error, retrying logging into " +  skyboxurl)
                    traceback.print_exc()
                    loginStatus = s.login(skyboxurl) 

                try:
                    #perform the upload to influxdb in the cloud
                    write_api = client.write_api(write_options=SYNCHRONOUS)
                    write_api.write(bucket, org, infuxInsertString.rstrip(','))
                    logIt("uploaded to influxDB -> " + statusMsg)

                except:
                    #something bad happened, error uploading to influx
                    traceback.print_exc()
            
                #now that we've done a loop and uploaded data for the time step, lets sleep and then start again with the next loop
                time.sleep(sleeptime)
                
        except:
            #something unexpected happened, lets wait a minute and start all over.
            traceback.print_exc()
            time.sleep(60) 
 
    
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if __name__ == '__main__':
    sys.exit(main())
