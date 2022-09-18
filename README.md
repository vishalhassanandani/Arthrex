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
To understand how to run puthon testcase refere document at https://dev.to/juperala/how-to-run-robot-framework-test-from-command-line-5aa

for simple run,go to the project folder & execute command below mention in 


```
robot [options] robot_files
robot -d result -t All main/test/API
```


## Reports
For better illustration on the testcases, reports has been generated under the `result/`
 


## Creating a test file
* Tests can be created directly within the `main/test/API/ or main/test/UI/` folder 

 
### Booking application Test cases 
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

5.get booking details by checkin and checkout dates (Note: not able to set date object in json)
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

