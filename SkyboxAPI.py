#!/usr/bin/env python3
import sys
import requests
import json
'''
Created on Aug 20, 2021
@author: zack
'''




class SkyboxAPI(object):
    def __init__(self):
        '''
        Constructor
        '''
        self.session = requests.Session()
        self.username = "I"
        self.password = "skybox"
        self.url = "http://192.168.1.142:3000"
        
    def login(self,url,username="I",password="skybox"):    
        '''
        Login, by default use the factory credentials, or you can supply them.
        '''
        self.url = url
        self.username = username
        self.password = password
        loginInfo = {'username': username,'password': password}
        response = self.session.post(url + "/authenticateuser/login",data=loginInfo)
        return response.json()

    def getSkyboxURLGET(self,url):
       response = self.session.get(url)
       return response.json()

    def getSkyboxURLPOST(self,url):
       response = self.session.post(url)
       return response.json()

    def getStatus(self):
        all = self.getSkyboxURLGET(self.url + "/donutstatus/read")
        all.update(self.getSkyboxURLPOST(self.url + "/pvstatus/readPersistenceStatus"))
        all.update(self.getSkyboxURLPOST(self.url + "/inverterstatus/readStatus"))
        return all

    def getAlerts(self):
        return self.getSkyboxURL(self.url + "/systemlog/alertStatus") 

    def getNotifications(self):
        return self.getSkyboxURL(self.url + "/systemlog/readnotification")

 

 

