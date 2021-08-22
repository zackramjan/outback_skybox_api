#!/usr/bin/env python3
import json
import sys
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

    # iterate over all the entries and display them in a wikimarkup formated style
    for metric in sorted(status):
        if not metric.endswith("_property"):
            print("## " + metric)
            print("#### Example")
            print("```python")
            print("import json")
            print("import SkyboxAPI")
            print("s = SkyboxAPI.SkyboxAPI()")
            print("status = s.getStatus()")
            print("print('The value of " + metric + " is ' + status['" + metric +"'])")
            print("```")
            print("> the value of " + metric + " is " + status[metric])
            print()
            print("### Description")
            if metric + "_property" in status:
                print(printProperty(status,metric + "_property","type"),end ="")
                print(printProperty(status,metric + "_property","default"),end ="")
                print(printProperty(status,metric + "_property","unitOfMeasure"),end ="")
                print(printProperty(status,metric + "_property","scalingFactor"),end ="")
                print(printProperty(status,metric + "_property","decimalScale"),end ="")
                if "enumOptions" in status[metric + "_property"]:
                    print("#### Possible Values (Enumeration)")
                    for e in status[metric + "_property"]["enumOptions"]:
                        print("* " + str(e["Value"]) + " -> " + str(e["Name"]))
            else:
                print("*No further details available*")
            
            print()
            print()



def printProperty(status,metric_property,attr):
    if metric_property in status:
        if attr in status[metric_property]:
            return "**" + str(attr) + ":** " + str(status[metric_property][attr]) + "<br/>\n"
    return ""



if __name__ == '__main__':
    sys.exit(main())