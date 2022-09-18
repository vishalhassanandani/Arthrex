from robot.api import logger
from robot.output import librarylogger

#from robotremoteserver import RobotRemoteServer

def write(msg, level='INFO', html=False):
    librarylogger.write(msg, level, html)
    with open('log.txt', 'a') as f:
        print(f'{level}\tHH:MM:SS > {msg}', file=f)

class LoggerConsole():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 0.1
    #logger = None

    def __init__(self, to_file=True):
        if to_file:
            logger.write = write


    def debug(self,msg):
        logger.console(msg)
        logger.debug(msg)

    def info(self,msg):
        logger.console(msg)
        logger.info(msg)

    def warn(self,msg):
        logger.console(msg)
        logger.warn(msg)

    def error(self,msg):
        logger.console(msg)
        logger.error(msg)


