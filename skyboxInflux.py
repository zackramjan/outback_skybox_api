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


def main(argv=None): 
    while True:
        try:
            token,org,bucket,url,skyboxurl,sleeptime = readConfig()
            client = InfluxDBClient(url=url, token=token, verify_ssl=False)
            
            s = SkyboxAPI.SkyboxAPI()
            logIt("logging into " +  skyboxurl)
            loginStatus = s.login(skyboxurl) 
            while True:
                try:
                    token,org,bucket,url,skyboxurl,sleeptime = readConfig()
                    status = s.getStatus()
                    alert =  s.getAlerts()[0]
                    notifcation =  s.getNotifications()[0]
                    infuxInsertString = "skybox lastNotice=\"" + str(datetime.fromtimestamp(int(notifcation["Timestamp"])/1000))  + " " + notifcation["Message"] + "\","
                    infuxInsertString += "lastAlert=\"" +  str(datetime.fromtimestamp(int(alert["Timestamp"])/1000))  + " " + alert["Message"] + "\","
                    statusMsg = "PV_WATTS=" + str(float(status["pv_output_power_dc"])) + " PV_VOLTS=" + str(float(status["pv_pmb_voltage"])) + " GRID_WATTS=" + str(float(status["grid_realtime_wattage_sum"])) + " BATT_WATTS=" + str(float(status["battery_watts"])) + " BATT_VOLTS=" + str(float(status["battery_voltage"])) + " BATT_SOC=" + str(float(status["battery_state_of_charge"]))
                    
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
                    write_api = client.write_api(write_options=SYNCHRONOUS)
                    write_api.write(bucket, org, infuxInsertString.rstrip(','))
                    logIt("uploaded to influxDB -> " + statusMsg)

                except:
                    traceback.print_exc()
    
                time.sleep(sleeptime)
                
        except:
            traceback.print_exc()
            time.sleep(60) 
 
    
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if __name__ == '__main__':
    sys.exit(main())