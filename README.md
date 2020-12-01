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

The City is a string data type that needs to be sent from the HTML document, the value is captured at the backend of the project where a request will be made to 
a free weather API to get the weather data. This value will be part of the query string.

#### 2.1.1 From and To Time

Both values are also sent from the HTML document, which are received as string at the backend. These strings needs to be converted as timestamp values,
in order to filter the result received from the weather API request. These both determine the period in which the result, weather details of a certain
city is needed. Validations are done at the front-end and back-end, base on the following requirements:
- From Time cannot be greather than To Time
- To Time cannot be less than From Time
- Input Values must be corretly converted into timestamp
- From Time cannot be less than the current time as there is not historical data
- From and To Time has to be within the same day, as the interval required is an hourly inputs format
   
### 2.2 Outputs

#### 2.2.1 Temperature, Min-Temperature, Max-Temperature and Average temperature

Based on the weather data of the city requested and the interval data provided, the API is able  to consolidate temperature, min-temperature,
max-temperature in  arrays where their values are calculated respectively.

#### 2.2.2 Median temperature and humidity

From Temperature and humidity arrays, both median temperature and humidity are calculated using median statistics method to find a median value of an array of numbers.

## 3. Folders and Moulules

### 3.1 restapione

This is the main project file, where Django project was started. The folder is the heart of the django application. Files and directories inside will be a topic to discuss some other time

### 3.2 weather

This folder is the application that was created to only run the weather API project that we are talking about, migrations and templates directories are used; for view rendering 
and database relation with the Django application

Severals files were added based on the requirements, methodology and approach to the problem

## 4. How to run the code

#### 4.1 Clone this repo 
        The repository of this project need to be cloned into your desired location

#### 4.2 Virtual Environment 
        Create a venv for your project and add an .env file in same directory with your manage.py

#### 4.2 GET API key 
        Get an api key from Open Weather Map and generate a secret key for your django application. If you have issue to get this done,feel free to reach out,an .env file will be provided
 
#### 4.3 Requirementfile, 
        From your CMD run `pip install requirements.txt` to install all the dependancies of this project

#### 4.4 Migrations and Packages
        Do your migrations and package's installations, as the expectation is that the User is able to start a Django application on local machine

#### 4.5 Runserver
        Once your venv is actived, the migrations are done and all dependancies installed, nagivate to the directory of your manage.py then run `python manage.py runserver`
        
## 5 Working with the API

### 5.1 On Postman

postman can be used to get the response of this API, once the program or server is running on a certain port, mostly on `127.0.0.1:800`
the folliwng link can be used on postman to request data : `http://127.0.0.1:8000/api`
NB: the request type must be a POST, the body has to be raw and JSON data type must be selected. Please format your body as JSON as below example:
{
	"city": "cape town",
	"from_time": "22:45",
	"to_time": "23:50"
}

### 5.2 On Browser:

Once server is running on a port; by default :`http://127.0.0.1:8000/` will be the home page.
Click on send button to request the data from the API. AJAX call will be made to the backend.

If inputs are valid, a Chart will be plotted below the form with the requested city weather's data based on the hours interval
otherwise, Alert message is displayed to indicate the error

## 6 genral comments and future plan

- The weather API used in this project is Open Weather,an API key is needed before making call to their weather API system.

- The data retrieved from the request made to the API showed that, data are updated in an interval of 3 hours. Therefore, if the interval entered by the user is less than 3 hours and no data was retrieved in that period. The system make a single call to the Open Weather API in order to get an hourly data.
 
- The Extra will be added in near future.
   







