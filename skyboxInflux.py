#!/usr/bin/env python3
import json
import sys
import time
import datetime  
import traceback
from datetime import datetime
import ConfigParser
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import SkyboxAPI


#this is an example usage of the SkyboxAPI to retrieve and print various metrics
def main(argv=None): 


    token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=="
    org = "xxxxx@gmail.com"
    bucket = "xxxxx's Bucket"

    client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, verify_ssl=False)

    
    s = SkyboxAPI.SkyboxAPI()
    loginStatus = s.login("http://192.168.1.142:3000") 
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
            loginStatus = s.login("http://192.168.1.142:3000") 
        print(infuxInsertString)
        try:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(bucket, org, infuxInsertString.rstrip(','))
        except:
             traceback.print_exc()

        time.sleep(60)



if __name__ == '__main__':
    sys.exit(main())