import logging
import requests
import json
import os
import sys
import threading
from main.src.config.log import LoggerConsole
from typing import Tuple
#from main.src.config.project_config import *
from robot.api.logger import *


class baseClient:
    log = None
    sessionID= ''
    threadmanager = {}
    def __init__(self):
        self.endpoint = ""
        self.username = ""
        self.password = ""
        self.log = LoggerConsole()
        #BuiltIn().log_to_console("My Name is Vishal")
        #if self.threadmanager.get(threading.currentThread().ident) == None:
            #sessionID = self.login()
            #self.threadmanager.__setitem__(threading.currentThread().ident,sessionID)
            #print('The value of token id is {}'.format(sessionID))

        #print(f'project type is {projectType}')
        #print(f'environment is {environment}')
        #self.env = os.environ.get('ENV', environment)
        #self.project = os.environ.get('PROJECT', projectType)

        #url = API_HOSTS[self.project ][self.env]['baseurl']
        #self.base_url = self.endpoint
        #print(f'The base URL for {self.env} environment for project {self.project} is {self.base_url}')
        #self.username = API_HOSTS[self.project ][self.env]['username']
        #self.password = API_HOSTS[self.project ][self.env]['password']
        #self.username = self.username
        #self.password = self.password

    def setSession(self,key: str,value: str):
        self.log.info(f"Login with session ID {value}")
        os.environ['auth_key'] = key
        os.environ['auth_value'] = value

    def getendpoint(self) -> str:
        return os.getenv('endpoint')



    def getheader(self):
        headers = {"Content-Type": "application/json"}
        if os.getenv('auth_key') != None:
            headers.__setitem__(os.getenv('auth_key'), os.getenv('auth_value'))
        else:
            self.log.warn(f'No auth is been set for request')
        return headers


    def assert_status_code(self, caller_method):
        if self.status_code != self.expected_status_code:
            self.log.error(f"{caller_method}::Expected {self.expected_status_code}, Actual Status code : {self.status_code} for URL: {self.url}, Responce Json {self.rs_json}")
        else:
            self.log.info(f"{caller_method}::Expected {self.expected_status_code}, Actual Status code : {self.status_code} for URL: {self.url}, Responce Json {self.rs_json}")


    def post(self, endpoint, headers=None, payload=None, expected_status_code=200, params=None):
        self.url = self.getendpoint() + endpoint
        self.log.info(f"The URL is {self.url}")
        if not headers:
            headers = self.getheader()
        print(json.dumps(payload))
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        if rs_api.content != b'' and 'error' not in str(rs_api.content).lower():
            self.rs_json = rs_api.json()
        else:
            self.rs_json = rs_api.content
        self.assert_status_code(sys._getframe().f_back.f_code.co_name)
        self.log.debug(f"POST API response: {self.rs_json}")
        return self.rs_json

    def delete(self, endpoint, headers=None, payload=None, expected_status_code=500):
        self.url = self.getendpoint() + endpoint
        self.log.info(f"The URL is {self.url}")
        if not headers:
            headers = self.getheader()
        rs_api = requests.delete(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        try:
            self.rs_json = rs_api.json()
        except:
            self.rs_json = rs_api.content
        self.assert_status_code(sys._getframe().f_back.f_code.co_name)

        self.log.debug(f"DELETE API response: {self.rs_json}")

        return self.rs_json


    def get(self, endpoint, headers=None, expected_status_code=200, payload=None, params=None):
        self.url = self.getendpoint() + endpoint
        self.log.info(f"The URL is {self.url}")
        if not headers:
            headers = self.getheader()
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        try:
            self.rs_json = rs_api.json()
        except:
            self.rs_json = rs_api.content
        #if rs_api.content != b'' and 'error' not in str(rs_api.content).lower() and ' not authorized to access url' not in rs_api.content:
            #self.rs_json = rs_api.json()
        #else:
            #self.rs_json = rs_api.content
        self.assert_status_code(sys._getframe().f_back.f_code.co_name)
        self.log.debug(f"POST API response: {self.rs_json}")
        print(type(self.rs_json))
        return self.rs_json

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        self.url = self.getendpoint() + endpoint
        self.log.info(f"The URL is {self.url}")
        if not headers:
            headers = self.getheader()
        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        if rs_api.content != b'' and 'error' not in str(rs_api.content).lower():
            self.rs_json = rs_api.json()
        else:
            self.rs_json = rs_api.content
        self.assert_status_code(sys._getframe().f_back.f_code.co_name)
        self.log.debug(f"PUT API response: {self.rs_json}")
        return self.rs_json


