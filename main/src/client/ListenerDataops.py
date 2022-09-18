from robot.libraries.BuiltIn import BuiltIn

from main.src.client.baseClient import *


class ListenerDataops(baseClient):
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def _start_suite(self, name, attrs):
        message = "hello, world"
        BuiltIn().log("This is My first Listener")
        BuiltIn().set_suite_variable("${from listener}", message)

    def start_test(self, name, attrs):
        time = BuiltIn().get_time()
        print(f'Executing testcase \'{name}\' start time is {time}')


