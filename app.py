import sqlite3
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates") # Создание экземпляра приложения Flask

# Создаем базу данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY, username TEXT, balance INTEGER)''')
cursor.execute('''INSERT OR IGNORE INTO users (username, balance) VALUES ('user1', 5000)''')
cursor.execute('''INSERT OR IGNORE INTO users (username, balance) VALUES ('user2', 6000)''')
cursor.execute('''INSERT OR IGNORE INTO users (username, balance) VALUES ('user3', 7000)''')
cursor.execute('''INSERT OR IGNORE INTO users (username, balance) VALUES ('user4', 8000)''')
cursor.execute('''INSERT OR IGNORE INTO users (username, balance) VALUES ('user5', 9000)''')
conn.commit()

class User:
    def __init__(self, id, username, balance): # Инициализация объекта класса User
        self.id = id
        self.username = username
        self.balance = balance

    def add_user_to_db(self): # Метод для добавления пользователя в базу данных
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (id, username, balance) VALUES (?, ?, ?)', (self.id, self.username, self.balance))
        connection.commit()
        connection.close()

    def update_balance(self, new_balance): # Метод для обновления баланса пользователя
        if new_balance >= 0:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, self.id))
            connection.commit()
            connection.close()

    @staticmethod # Статический метод для получения пользователя по ID
    def fetch_user_by_id(user_id):
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        connection.close()
        return user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_balance', methods=['POST']) # Маршрут для обновления баланса через POST запрос
def update_balance():
    user_id = request.form['userId'] # Получаем параметр userId из POST
    city = request.form['city'] # Получаем параметр city из POST запроса
    key = "a6ff5de48bf8e773bf34de625fb6630e"
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}') #Получаем данные о погоде
    data = response.json()
    temperature = data['main']['temp'] # Получаем температуру из данных о погоде

    user = User.fetch_user_by_id(user_id) # Получаем пользователя из базы данных
    if user:
        current_balance = user[2] # Получаем текущий баланс пользователя
        new_balance = current_balance + temperature # Вычисляем новый баланс
        user_obj = User(user[0], user[1], current_balance)  # Создаем экземпляр класса User с текущим балансом
        user_obj.update_balance(new_balance) # Обновляем баланс пользователя

    return f'The balance for the user has been updated, see the result\n{user_id, new_balance}'


if __name__ == '__main__':
    app.run()