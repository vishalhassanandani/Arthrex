from robot.api.deco import keyword
from main.src.client.client import client
from main.src.lib.project_config.project_config import *
from main.src.lib.API.payload.login import *
from main.src.lib.API.Pages.endpoints import *

class apiLogin(client):
    def __init__(self):
        super(apiLogin, self).__init__()
        self.config = project_config()


    @keyword("Login to the booking application")
    def login_to_application(self, username, password):
        self.log.info('------------login to the application------------')
        os.environ['endpoint'] = self.config.gethost()
        data: dict = credentials(username,password)
        responce = self.post(endpoint=login, payload=data, expected_status_code=200)
        auth_token = responce.get('token')
        self.setSession('cookie',f'token={auth_token}')


