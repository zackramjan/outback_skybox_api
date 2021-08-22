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

    def getStatus(self):
        response = self.session.get(self.url + "/donutstatus/read")
        return response.json()

    def getAlerts(self):
        response = self.session.get(self.url + "/systemlog/alertStatus") 
        return response.json()

    def getNotifications(self):
        response = self.session.get(self.url + "/systemlog/readnotification")
        return response.json()

    def getPersistantStatus(self):
        response = self.session.get(self.url + "/pvstatus/readPersistenceStatus")
        return response.json()

    def getInverterStatus(self):
        response = self.session.get(self.url + "/inverterstatus/readStatus") 
        return response.json()
