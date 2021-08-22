#!/usr/bin/env python3
import SkyboxAPI
import json
import sys

#this is an example usage of the SkyboxAPI to retrieve and print various metrics
def main(argv=None): 
    #make sure you have enabled remote login in Global SEttings -> System -> Remote Security -> Enable Remote Login. 
    s = SkyboxAPI()

    # The web interface will be running on port 3000. you can check your  skybox IP address on the skybox in the Global Settings -> Network
    # It will attempt to use the outback default remote access account of username = "I" and password = "skybox"
    # You can change this to a custom usrename password like this:
    # loginStatus = s.login("http://192.168.1.142:3000","I","mypassword") 
    # this will log you into the skybox and allow you to perform further inquiries
    loginStatus = s.login("http://192.168.1.142:3000") 
    # optionally, we can save and print the login status 
    # loginStatus = s.login("http://192.168.1.142:3000") 
    # print(loginStatus)
    
    #Lets get the current status and print a few metrics
    status = s.getStatus()
    print(status['pv_status'])

    #for every metric, there is usally and metric_property which describes the values the metric returns
    print(status['pv_status_property'])

    print(status['load_combined_wattage_sum'])
    print(status['load_combined_wattage_sum_property'])


if __name__ == '__main__':
    sys.exit(main())