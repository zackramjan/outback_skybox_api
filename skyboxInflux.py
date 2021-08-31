#!/usr/bin/env python3
import json
import sys
import time
import datetime  
import traceback
from datetime import date, datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
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
            print("logging into " +  skyboxurl)
            loginStatus = s.login(skyboxurl) 
            while True:
                try:
                    status = s.getStatus()
                    infuxInsertString = "skybox "
                    for e in sorted(status):
                        if not e.endswith("_property"):
                            try:
                                val = float(status[e])
                                infuxInsertString += e + "=" +  status[e].lower() + ","
                            except:
                                pass
                except:
                    print("error, retrying logging into " +  skyboxurl)
                    loginStatus = s.login(skyboxurl) 
                try:
                    write_api = client.write_api(write_options=SYNCHRONOUS)
                    write_api.write(bucket, org, infuxInsertString.rstrip(','))
                    print( str(datetime.now()) + ": uploaded to influxDB -> " + infuxInsertString[0:50] + "..." + infuxInsertString[-50:])
                except:
                    traceback.print_exc()
    
                time.sleep(sleeptime)
        except:
            traceback.print_exc()
            time.sleep(60) 
 
    
    

if __name__ == '__main__':
    sys.exit(main())