import configparser
from main.src.config.log import LoggerConsole

class config_reader:
    section = None
    def __init__(self, section, fileName):
        self.section = section
        print(self.section)
        self.fileName = fileName
        self.log = LoggerConsole()
        self.reader_config = configparser.ConfigParser()
        self.reader_config.read(self.fileName)

    def getValue(self,key: str) -> str:
        try:
            value = self.reader_config.get(self.section,key)
            #self.log.info(f"{key} : {value}")
        except Exception as e:
            self.log.error(e)
        return value

    def getProject(self):
        return self.getValue('project').upper()

    def getEnv(self):
        return self.getValue('environment')

    def getHost(self):
        return self.getValue('host')

    def getUsername(self):
        return self.getValue('userName')

    def getPassword(self):
        return self.getValue('password')


    def getLocator(self, key: str) -> str:
        return self.getValue(key)

    def get_value(self, param):
        pass
