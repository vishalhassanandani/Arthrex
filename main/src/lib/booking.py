try:
    from main.src.client.ListenerDataops import *
    from main.src.client.RobotFrameworkListener import *
    from main.src.data.read_data import *
    from main.src.client.baseClient import *
    from main.src.lib.API.Pages.apiLogin import *
    from main.src.lib.API.Pages.apiBooking import *

except Exception as e:
    print("Vishal Hassanandani")
    print(e)


class booking(
    ListenerDataops,
    RobotFrameworkListener,
    read_data,
    apiLogin,
    apiBooking

):
    """
    This library will provides keywords to automating the TSPS cloud test cases
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        for base in booking.__bases__:
            base.__init__(self)


