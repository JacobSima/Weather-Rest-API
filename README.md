# Weather-Rest-API
Python Weather API build with Django Rest

## 1. Description

### 1a. User Story

As an API user I want to get min, max, average and median temperature and humidity for given city and period of time

### 1b. Requirements

Use git for version control

publish on GitHub or send us a compressed repo

### 1c. Functionality

create locally running RESTful web API

django-rest-framework recommended, though not necessary

that accepts a request with 'city' and 'period' args

fetches weather data for that location and period of time from some public API

e.g. Yahoo! Weather

computes min, max, average and median temperature and humidity for that location and period and returns that to the user

### 1d.Extra goals

Provide a view which renders a bar chart for the requested data

Deploy it somewhere


## 2. Problem Inputs and Outpus

### 2.1 Inputs

#### 2.1.1 City

The City is a string data type that needs to be sent from the HMTL document, the value is captured in the backend of the project where a request will be made to 
a free weather API to get the weather infromation. This value will be part of the query string.

#### 2.1.1 From and To Time

Both values are also sent from the HTML document, which are recieved as string at the backend. These strings needs to be convert into a value time stamp,
in order to filter the result recieved from the weather API request. These value determined the period in which the result are or weather details of a certain
city is needed. Validates are done at the front-end and back-end, base on the following requirements:
        * From Time cannot be greather than To Time
        * To Time cannot be less than From Time
        * Input Values must be corretly convert into a valid timestamp
        * From Time cannot be less than the current time as there is not historical data
        * From and To Time has to be within the same day, as the interval required is an hourly inputs formats
   
### 2.2 Outputs

#### 2.2.1 Temperature, Min-Temperature, Max-Temperature and Average temperature

Based on the weather data of the city requested and the interval data provided, the API is able  to consolidate temperature, min-temperature,
max-temperature in  arrays where their values are calculated respectively.

#### 2.2.2 Median temperature and humidity

From Temperature and humidity arrays, that were both median temperature and humidity were calculated using median statistics method to find a median valud of an array of numbers.

## 3. Folders and Moulules

### 3.1 restapione

This is the main project file, where the Django project was started. The folder is heart of the django application. Files and directories inside will be a topic to discusss 
in another time

### 3.2 weather

This folder is the application that was created to only runs the weather API project that we are talking about, migrations and templates directories are used; for view rendering 
and database relation with the Django application

Severals files were added based on the requirements, methodology and approch to the problem


## 4. How to run the code

#### 4.1 Clone this repo 
        The repository of this project need to be clone into your desired location

#### 4.2 Create virtual environment for your project and add a .env file in same directory with your manage.py

#### 4.2 GET API key from Open Weather Map and generate a secret key for your django application. If you have issue to get this done,
         feel free to provide you with my .env file
 
#### 4.3 Run requirement.txt file, from your CMD run `pip install requirements.txt` to install all the dependancies of this project

#### 4.4 Do your migrations and all, as we are expecting to be ready to start or fix buggs on a Django application

#### 4.5 Runserver, once your venv is actived, the mogrations are done and all dependancies installed, nagivate to the directory of your manage.py
        then run `python manage.py runserver`
        
## 5 Working with the API

### 5.1 On Postman

postman can be used to get the response of this API, once the program or server running to a certain port, mostly on 127.0.0.1:800
the folliwng link can be used on postman to request data : `http://127.0.0.1:8000/api`
NB: the request type must a POST, the body has to be raw and JSON data type must be selected. Please format your body as JSON as below example:
{
	"city": "cape town",
	"from_time": "22:45",
	"to_time": "23:50"
}

### 5.2 On Browser:

Once server running on a port, by default :`http://127.0.0.1:8000/` will be the home page
Input valid data or do test data then click the send button. An ajax request is made to the backend to query data
base on the form input values.

If all is valid, a Chart will be plot below the form with the requested city weather's information based on the hours interval
If all not valid, Alert message is displayed to indicate the error

## 6 genral comments and future plan

- The Open Weather request made, provided data in an iterval of 3 hours, meaning if the interval if less than 3 hours. This code is provinding the avalaible data
  get the request of the current hour. The API weather application is working and the basics requested from the User are 
 
- The Extra will be added in near future.
   







