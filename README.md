# Robot Framework-Python
Robot Framework is a generic open source automation framework. This framework is created to use the python library from the robot framework, this help us to overcome the limitations of robot framework & use the most of both technology.

## Supports
* Rest API automation
* UI Automation (Placeholder is created)
* Reports


## Setup
* Clone this repository
* Navigate to the cloned folder
* To install the dependencies in MAC we use Homebrew version manager install (using)[https://brew.sh/]
* Once brew is installed install python by `brew install python3`
* To get additional dependencies of python like pip3, do `brew postinstall python3`
* Install the required packages needed for this framework using `pip3 install -r requirements.txt`
* Install the custom package python setup.py install
* 
## To Run the tests
For a simple run of all the test files in normal mode, try

go to the project folder & execute command below mention in https://dev.to/juperala/how-to-run-robot-framework-test-from-command-line-5aa


```
robot [options] robot_files
robot -d result -t All main/test/dataops/API
```


## Reports
For better illustration on the testcases, reports has been generated under the `result/`
 


## Creating a test file
* Tests can be created directly within the `main/test/API/ or main/test/UI/` folder with the file prefix as `test_` so that those files alone will be taken during test run. This is configured in `pytest.ini` file.

### Simple test case with an endpoint

The application host can be updated from 'main/src/lib/project_config/config.ini' 
we can switch between multiples environment by switching the environment from config file

```
Api.get("/name")
Api.verify_response_code(200)
```
On calling only these two methods from the `Api` library, all the allure report actions, attaching the request and the response file to the reports, and asserting the response code of the response is taken care off.

### Simple test case with validating the response with test data

To validate the response json with a test data, one could do the following,

 
### Booking Test cases 
booker assignment testcase can be found at 'main/test/API/booking.robot'

1. Login to the application
    Login to the application with default usernam & password
    Set the token id in the header.

2. Create the new booking
   generate random data to create new order
   create new order with randomly generated data
   get all the list of id & validate that our newly created booking id exist
   search booking base on id & validate with our generated data

3. update the booking
   generate random data to update new order
   update the booking with updated data
   get booking details for the given booking id
   validate booking is created with the given details

4.get booking details by firstname & lastname
  generate the filter data by first name & lastname
  search the booking base of filter
  validate that you get the expected booking id

5.get booking details by checkin and checkout dates (Note: teas case is failing as there is issue with application)
  generate the filter data by checkin & checkout date
  search the booking base of filter
  validate that you get the expected booking id

6. delete the booking
   deleted the booking by booking id
   search all the booking
   validate that booking  deleted does not exist

Note: results are saved under 'result\report.html'
logs are saved under 'result\log.html'

## Authors

* **[Vishal Hassanandani]()**

