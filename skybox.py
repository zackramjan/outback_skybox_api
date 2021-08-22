#!/usr/bin/env python3
import json
import sys
import datetime  
import SkyboxAPI

#this is an example usage of the SkyboxAPI to retrieve and print various metrics
def main(argv=None): 
    # make sure you have enabled remote login in Global Settings -> System -> Remote Security -> Enable Remote Login. 
    s = SkyboxAPI.SkyboxAPI()

    # The web interface will be running on port 3000. you can check your skybox IP address on the skybox in the Global Settings -> Network
    # It will attempt to use the outback default remote access account of username = "I" and password = "skybox"
    # You can change this to a custom userename password like this:
    # loginStatus = s.login("http://192.168.1.142:3000","I","mypassword") 
    # this will log you into the skybox and allow you to perform further inquiries
    loginStatus = s.login("http://192.168.1.142:3000") 
    # optionally, we can save and print the login status 
    # loginStatus = s.login("http://192.168.1.142:3000") 
    # print(loginStatus)
    
    # Lets get the current status and print a few metrics
    status = s.getStatus()

    # display the status of the pv input
    # the status is a value from 0 to 6
    print(status['pv_status'])

    # for every 'metric', there is usually a corresponding 'metric_property' which describes the range of values the metric returns.
    # here we can see that 1 means "producing" and 3 means "sleeping"
    print(status['pv_status_property'])

    #print the load from the load panel
    print(status['load_combined_wattage_sum'])

    #printing the corresponding property, describes the units etc
    print(status['load_combined_wattage_sum_property'])

    #print the load from the load panel
    print(status['inverter_current_status'])

    #printing the corresponding property, describes the units etc
    print(status['inverter_current_status_property'])

    #get and print the Alerts, these are the red-marked alerts from the skybox graphical interface
    for alert in s.getAlerts():
        print(str(alert["fileIndex"]) + " " + str(datetime.datetime.fromtimestamp(int(alert["Timestamp"])/1000))  + "\t" + alert["Message"])

    #get and print the Notifcations, these are the in the "log" section of the skybox graphical interface
    for notifcation in s.getNotifications():
        print(str(notifcation["fileIndex"]) + " " + str(datetime.datetime.fromtimestamp(int(notifcation["Timestamp"])/1000))  + "\t" + notifcation["Message"])

if __name__ == '__main__':
    sys.exit(main())