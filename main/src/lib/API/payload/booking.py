from faker import Faker
from datetime import datetime
import random
import datetime
import json
def generate_payload_by_filter(filter: dict) -> dict:
    filter_data = {}
    #format = '%Y-%m-%d'
    for key,value in filter.items():
        if key.lower() == 'firstname':
            filter_data.__setitem__('firstname',value)
        if key.lower() == 'lastname':
            filter_data.__setitem__('lastname',value)
        if key.lower() == 'checkin':
            #checkin_date=datetime.datetime.strptime(value, format)
            #json_datetime = json.dumps(checkin_date.date())
            #checkin= checkin_date.date().fromisoformat(value)
            filter_data.__setitem__('checkin',value)
        if key.lower() == 'checkout':
            #checkout_date = datetime.datetime.strptime(value, format)
            #json_datetime = json.dumps(checkout_date.date())
            #checkout = checkout_date.date().fromisoformat(value)
            filter_data.__setitem__('checkout',value)
    return filter_data

def create_booking_data() -> dict:
    faker = Faker()
    create_booking: dict = {}
    bookingdates: dict = {}
    checkInDate = str(faker.date_time_between(start_date="-100d", end_date="-50d"))[:10]
    checkOutDate = str(faker.date_time_between(start_date="-49d", end_date="now"))[:10]
    #date_range= faker.date_between_dates(date_start=datetime(2015, 1, 1), date_end=datetime(2019, 12, 31)).year
    bookingdates.__setitem__('checkin', checkInDate)
    bookingdates.__setitem__('checkout', checkOutDate)
    create_booking.__setitem__('firstname',faker.first_name())
    create_booking.__setitem__('lastname', faker.last_name())
    create_booking.__setitem__('totalprice', random.randint(100, 900))
    create_booking.__setitem__('depositpaid', bool(random.getrandbits(1)))
    create_booking.__setitem__('bookingdates', bookingdates)
    create_booking.__setitem__('additionalneeds', random.choice(['Breakfast', 'Lunch', 'Dinner']))
    return create_booking


