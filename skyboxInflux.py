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
from pyHS100 import SmartPlug, SmartBulb
import SkyboxAPI

#this is an example usage of the SkyboxAPI to retrieve and print various metrics
def main(argv=None): 
    while True:
        try:
            f = open('config.json', "r") 
            config = json.load(f)
            token = config["token"]
            org = config["org"]
            bucket = config["bucket"]
            url = config["url"]
            skyboxurl = config["skyboxurl"]
            sleeptime = int(config["sleeptime"])
    
            client = InfluxDBClient(url=url, token=token, verify_ssl=False)
            
            s = SkyboxAPI.SkyboxAPI()
            print("logging into " +  skyboxurl, file=sys.stderr)
            loginStatus = s.login(skyboxurl) 
            while True:
                try:
                    status = s.getStatus()
                    alert =  s.getAlerts()[0]
                    notifcation =  s.getNotifications()[0]
                    infuxInsertString = "skybox lastNotice=\"" + str(datetime.fromtimestamp(int(notifcation["Timestamp"])/1000))  + " " + notifcation["Message"] + "\","
                    infuxInsertString += "lastAlert=\"" +  str(datetime.fromtimestamp(int(alert["Timestamp"])/1000))  + " " + alert["Message"] + "\","
                    
                    for e in sorted(status):
                        if not e.endswith("_property"):
                            try:
                                val = float(status[e])
                                infuxInsertString += e + "=" +  status[e].lower() + ","
                            except:
                                pass
                    
                    #check for curtailment, and if so, add load via space heaters
                    try:
                        plug1 = SmartPlug("192.168.1.131")
                        plug2 = SmartPlug("192.168.1.132")
                        if(float(status['pv_bb_input_voltage']) > 350.0 and 
                            float(status['grid_realtime_wattage_sum']) > -700.0 and 
                            float(status['battery_watts']) > -70.0 and
                            float(status['battery_watts']) < 70.0
                        ):
                            if "OFF" in plug1.state:
                                plug1.turn_on()
                                print(str(datetime.now()) + "Turning kasa plug 1 on", file=sys.stderr)
                            elif "OFF" in plug2.state:
                                plug2.turn_on()
                                print(str(datetime.now()) + "Turning kasa plug 2 on", file=sys.stderr)
                        elif float(status['pv_bb_input_voltage']) > 200.0:
                            if "ON" in plug2.state:
                                plug2.turn_off()
                                print(str(datetime.now()) + "Turning kasa plug 2 off", file=sys.stderr)
                            elif "ON" in plug1.state:
                                plug1.turn_off()
                                print(str(datetime.now()) + "Turning kasa plug 1 off", file=sys.stderr)
                            
                    except:
                       print("Error changing space heater load (KASA PLUG 1 or 2)", file=sys.stderr) 
                       traceback.print_exc()





                                
                except:
                    print("error, retrying logging into " +  skyboxurl, file=sys.stderr)
                    traceback.print_exc()
                    loginStatus = s.login(skyboxurl) 
                try:
                    write_api = client.write_api(write_options=SYNCHRONOUS)
                    write_api.write(bucket, org, infuxInsertString.rstrip(','))
                    print( str(datetime.now()) + ": uploaded to influxDB -> " + infuxInsertString[0:50] + "..." + infuxInsertString[-50:], file=sys.stderr)
                except:
                    traceback.print_exc()
    
                time.sleep(sleeptime)
        except:
            traceback.print_exc()
            time.sleep(60) 
 
    
    
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if __name__ == '__main__':
    sys.exit(main())