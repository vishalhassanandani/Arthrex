try:
    from baseClient import *
except:
    from .baseClient import *

class client(baseClient):
    """
        This library will provides keywords to automating the TSPS cloud test cases
        """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        for base in client.__bases__:
            base.__init__(self)