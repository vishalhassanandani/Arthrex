import os
from main.src.config.config_reader import *
from main.src.config.log import LoggerConsole


class project_config(config_reader):
    def __init__(self):
        self.log = LoggerConsole()
        filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "project_config\\config.ini")
        self.log.debug(f"The config file path is {filepath}")
        self.conf = config_reader('DEFAULT', filepath)
        self.env = self.conf.getEnv().upper()
        self.conf = config_reader(self.env,filepath)
        #self.host = self.conf.getHost()
        #self.username = self.conf.getUsername()
        #self.password = self.conf.getPassword()
        #self.updateConfigParameters()

    def getcommandhost(self):
        return self.conf.getValue('command_host')

    def getvictoriahost(self):
        return self.conf.getValue('victoria_host')

    def gethost(self):
        return self.conf.getValue('host')

    def getapplicationUIURL(self):
        return self.conf.getValue('application_ui_url')


    def updateHost(self):
        if self.env is not None and self.host is not None:
            API_HOSTS[self.project.upper()][self.env.lower()]['baseurl'] = self.host
        else:
            self.log.error(f"environment is {self.env} & host is {self.host}")

    def updateUserName(self):
        if self.env is not None and self.username is not None:
            API_HOSTS[self.project.upper()][self.env.lower()]['username'] = self.username
        else:
            self.log.error(f"environment is {self.env} & host is {self.username}")


    def updatePassword(self):
        if self.env is not None and self.password is not None:
            API_HOSTS[self.project.upper()][self.env.lower()]['password'] = self.password
        else:
            self.log.error(f"environment is {self.env} & host is {self.password}")

    def updateConfigParameters(self):
        if self.host is not None:
            self.updateHost()
        if self.username is not None:
            self.updateUserName()
        if self.password is not None:
            self.updatePassword()


API_HOSTS = {
    'VRDM': {
        "qa": {
            "baseurl": "http://clm-aus-vdmrf7:30555",
            "username": "",
            "password": ""
        },
        "dev": {
            "baseurl": "http://clm-aus-vdmrf7:30555",
            "username": "",
            "password": "",
            "socket": None
        }
    }
}

apiheader = {
    "Content-Type": 'application/json'
}

blankheader = {}