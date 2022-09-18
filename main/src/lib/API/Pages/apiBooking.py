import collections
from robot.api.deco import keyword
from main.src.client.client import client
from main.src.lib.API.Pages.apiLogin import *
from main.src.lib.project_config.project_config import *
from main.src.lib.API.Pages.endpoints import *
from main.src.lib.API.payload.booking import *
from typing import List, Tuple


class apiBooking(client):
    def __init__(self):
        super(apiBooking, self).__init__()
        self.log = LoggerConsole()
        self.config = project_config()

    @keyword('get list of all booking id')
    def get_list_of_all_booking_ids(self) -> list:
        """
            get the list of all booking id
            :return list: list of booking id
        """
        self.log.info('-------------get booking ids-----------------')
        data: dict = {}
        responce = self.get(endpoint=booking, payload=data, expected_status_code=200)
        return responce

    def validate_booking_id_list_is_not_empty(self, list_of_booking_id: list) -> bool:
        """
            validate that the booking id list is not empth
            :param list_of_booking_id: list of booking id
            :return bool: true or false
        """
        if len(list_of_booking_id) > 0:
            return True
        else:
            return False

    @keyword('validate booking id exist')
    def validate_booking_id_exist(self,list_of_booking_id: list, bookingID: str) -> bool:
        """
            validate booking id exist
            :param list_of_booking_id: list of booking id
            :param bookingID: booking id to validate
            :return bool: true or false
        """
        self.log.info(f"the list of booking id is {list_of_booking_id}")
        self.log.info(f"the booking id is {bookingID}")
        for booking_id in list_of_booking_id:
            if booking_id.get('bookingid') == int(bookingID):
                return True
        return False

    @keyword('search the booking base of filter')
    def get_booking_id_by_filter(self,filter:dict) -> dict:
        """
            search the booking base on search criteria
            :param filter: search criteria for booking
            :return dict: return search response base on search criteria
        """
        self.log.info('---------------get booking details by filter-----------')
        data: dict = generate_payload_by_filter(filter)
        self.log.info(f"The search request is {data}")
        responce = self.get(endpoint=booking, payload=data, expected_status_code=200, params=filter)
        return responce

    @keyword('get booking details for the given booking id')
    def get_booking_details_by_id(self, booking_id: str) -> dict:
        """
            search the booking details for the booking id
            :param booking_id: booking id
            :return dict: booking details for the booking id
        """
        self.log.info('-----------get booking details by id-----------')
        data: dict = {}
        responce = self.get(endpoint=booking + '/' + booking_id, payload=data, expected_status_code=200)
        return responce

    @keyword('validate booking is created with the given details')
    def validate_booking_details(self, autual_booking: dict, expected_booking: dict) -> bool:
        """
            validate booking is created with the given details
            :param autual_booking: actual booking details
            :param expected_booking: expected booking details
            :return bool: true or false
        """
        self.log.info(f'Actual booking data is {autual_booking}')
        self.log.info(f'expected booking data is {expected_booking}')
        if collections.Counter(autual_booking) == collections.Counter(expected_booking):
            return True
        return False

    @keyword('create new booking')
    def create_new_booking(self) -> Tuple[dict,dict]:
        """
            create new booking
            :return dict: booking response
            :return dict: data for creating booking
        """
        self.log.info('----------create new booking--------------------')
        data: dict = create_booking_data()
        responce = self.post(endpoint=booking, payload=data, expected_status_code=200)
        return responce, data

    @keyword('update the newly created booking')
    def update_new_booking(self, booking_id: str) -> Tuple[dict, dict]:
        """
            update booking
            :param booking_id: booking id for which we need to update booking
            :return dict: updated booking response
            :return dict: data for updating booking
        """
        self.log.info('----------create new booking--------------------')
        data: dict = create_booking_data()
        responce = self.put(endpoint=booking + '/' + booking_id, payload=data, expected_status_code=200)
        return responce, data

    @keyword('delete the booking')
    def delete_booking(self, bookingID: str) -> dict:
        """
            delete booking
            :param bookingID: booking id for which we need to delete booking
            :return dict: delete booking response
        """
        self.log.info('-----------delete booking-----------')
        data: dict = {}
        responce = self.delete(endpoint=booking + '/' + bookingID, payload=data, expected_status_code=201)
        return responce

    @keyword('Get Dictionary Value')
    def get_value_from_dict(self, input: any, key: str):
        if type(input) == list:
            for data in input:
                return data.get(key)
        return input.get(key)

filter = {'checkin': '2022-07-10', 'checkout': '2022-08-27'}
apiLogin().login_to_application('admin','password123')
apiBooking().get_booking_id_by_filter(filter)