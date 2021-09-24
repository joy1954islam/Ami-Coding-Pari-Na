# Ami-Coding-Pari-Na

## Getting Started

* Installation Clone the repository : 
https://github.com/joy1954islam/Ami-Coding-Pari-Na.git

* Switch to the repo folder
	```cd Ami-Coding-Par-Na```

* Next you Install Virtualenv
	```pip install virtualenv```
* Create a virtual environment name env
	```virtualenv env```

* Active Your Virtualenv
```env/Scripts/activate```

* install the packages according to requirements.txt from the local archive directory
```pip install -r requirements.txt```


* Then Makemigrations Command
```python manage.py makemigrations```


* Migrate Command
```python manage.py migrate```

* Server Run Command
```python manage.py runserver```

* How to Token Generate
```
http POST http://127.0.0.1:8000/api-token-auth/ username='mdjoyislam' password='171-35-1954'

```
# Project Description:


You have to develop a web application. Your project will contain 3 sections.

# Section 1: User Authentication/Registration Page
A user login and registration section. You can use whatever input fields you want (maintaining a standard)

# Section 2: Khoj the search Page
 After login, users can access this page. 
 Khoj the search: In this segment(page), there will be two input fields
Input Values: User can input comma separated integers
Search Value: User can input only one integer 
Output: Will print True if the search value is in the input values. Otherwise print False

![sample](https://user-images.githubusercontent.com/43573718/134390293-ce98fc27-6678-419d-97e8-64dab8dd178e.PNG)

Now, before showing the output, you have to store the input values in the database in sorted order(descending) along with the logged in user id and the input timestamp. That means, when the user press the button “Khoj”, the Input values (9, 1, 5, 7, 10, 11, 0) will be stored in the database as follows : 11, 10, 9, 7, 5, 1, 0 

So the rough workflow for this section is as follows 

1. Take the “Input Values”
2. Take the “Search Value”
3. Sort the “Input values” in descending order.
4. Store the sorted “Input Values” in the database.
5. Check if the “Search Value” is in the “Input Values”
6. Print the output

Note: The above workflow might not be the optimal workflow. You can change your workflow as you need to make it more optimized.

# Section 3: API Endpoints
In this section, there will be only one API endpoints

Endpoint 1: Get All Input Values

Parameters: start_datetime, end_datetime, user_id

Returns: All the Input Values the user ever entered within start_datetime(inclusive) and end_datetime (inclusive). Check the following response format.
```

{
    “status”: “succes”,
    “user_id” : 1,
    “payload” : [
         {
              “timestamp” : ”2012-01-01 00:00:00”,
              “input_values” : “11, 10, 9, 7, 5, 1, 0”
          },
         {
                “timestamp” : ”2013-01-01 01:00:00”,
                 “input_values” : “13, 11, 10, 7, 5, 2, 1”
          
       ]
}

```


