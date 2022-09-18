*** Settings ***
Documentation    Testing the login functiolity of the application
Library     ../../../main/src/lib/booking.py
Variables    ../../../main/test/data/constant.py


*** Test Cases ***
Login to the application
    [Tags]    SANATY    ALL     BOOKING
    Login to the booking application    admin   password123

Create the new booking
    [Tags]    SANATY    ALL     BOOKING
    ${booking_responce}     ${booking_data}=    create new booking
    Set Global Variable     ${booking_responce}
    ${booking_id}=      Get Dictionary Value    ${booking_responce}     bookingid
    Set Global Variable     ${booking_id}
    ${list_booking_id}=     get list of all booking id
    ${check_id_exists}=     validate booking id exist  ${list_booking_id}   ${booking_id}
    Should be true      ${check_id_exists}         Fail to find booking id for created booking
    ${booking_details_by_id}=   get booking details for the given booking id    ${booking_id}
    ${check_booking_data}=      validate booking is created with the given details      ${booking_details_by_id}    ${booking_data}
    Should be true      ${check_booking_data}         Actual booking data ${booking_details_by_id} doesnot match with expected data ${booking_data}

update the booking
    [Tags]    SANATY    ALL     BOOKING
    ${updated_booking_responce}     ${updated_booking_data}=    update the newly created booking    ${booking_id}
    Set Global Variable     ${updated_booking_responce}
    ${booking_details_by_id}=   get booking details for the given booking id    ${booking_id}
    ${check_booking_data}=      validate booking is created with the given details      ${booking_details_by_id}    ${updated_booking_data}
    Should be true      ${check_booking_data}         Actual booking data ${booking_details_by_id} doesnot match with expected data ${updated_booking_data}

get booking details by firstname & lastname
    [Tags]    SANATY    ALL     BOOKING
    ${first_name}=      Get Dictionary Value    ${updated_booking_responce}     firstname
    ${last_name}=      Get Dictionary Value    ${updated_booking_responce}     lastname
    ${filter_by_name}=      Create Dictionary     firstname=${first_name}     lastname=${last_name}
    ${search_result}=   search the booking base of filter   ${filter_by_name}
    ${expected_booking_id}=      Get Dictionary Value    ${search_result}     bookingid
    Should be true      ${booking_id} == ${expected_booking_id}      Actual booking created with id ${booking_id} doesnot match with expected booking id ${expected_booking_id}

get booking details by checkin and checkout dates
    [Tags]    SANATY    ALL     BOOKING
    ${booking_dates}=    Get Dictionary Value    ${updated_booking_responce}    bookingdates
    ${checkin_date}=      Get Dictionary Value    ${booking_dates}     checkin
    ${checkout_date}=      Get Dictionary Value    ${booking_dates}    checkout
    Log  the checkin date is ${checkin_date}
    Log  the checkout date is ${checkin_date}
    ${filter_by_date}=      Create Dictionary     checkin=${checkin_date}     checkout=${checkout_date}
    Log  search creatria ${checkin_date}
    ${search_result}=   search the booking base of filter   ${filter_by_date}
    ${expected_booking_id}=      validate booking id exist  ${search_result}     ${booking_id}
    Should be true      ${expected_booking_id}      Fail to find booking id ${expected_booking_id} form search list ${search_result}

delete the booking
    [Tags]    SANATY    ALL     BOOKING
    ${deleted_responce}=       delete the booking      ${booking_id}
    ${list_booking_id}=     get list of all booking id
    ${check_id_exists}=     validate booking id exist  ${list_booking_id}   ${booking_id}
    Should not be true      ${check_id_exists}     fail to delete booking id ${booking_id}, search result is ${list_booking_id}