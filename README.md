Test task: Python WebApp Developer Create a web application using Flask When the application starts, a simple SQLite database is created to manage a list of users (users) with fields (id, username, balance) with 5 users and a balance from 5000 to 15000 Write a Python class User , which represents a user and interacts with the database to add, update, and delete users and update their balances. Using the requests library, write a function fetch_weather(city) that takes as input the name of a city and returns the current temperature in that city. Use any open API to get weather data. Important, you can use the error, the temperature changes no more than 10 minutes Write a route to update the user’s balance, both up and down by an amount equal to the air temperature in the selected city, which accepts the parameters userId, city. An important condition is that the user’s balance cannot be negative. Balance changes should be made in real time, without the use of queues and pending tasks.

Done:

Each time you run the app.py file, 5 more users with the specified balance are created in the database
The user's balance is updated depending on the weather in the selected city

To start the project you need:

1)Set up a virtual environment

2)Install dependencies by running the command (pip install -r requirements.txt)

3)Follow the link http://127.0.0.1:5000

4)Everything is ready - test it
