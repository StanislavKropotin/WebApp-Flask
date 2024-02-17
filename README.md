Тестовое задание: Python Разработчик
WebApp
Создать веб приложение используя Flask
При запуске приложения создается простая база данных SQLite, для управления списком пользователей(`users`) с полями(`id`, `username`, `balance`) с 5 пользователями и балансом от 5000 до 15000
Напишите Python-класс `User`, который представляет пользователя и взаимодействует с базой данных для добавления, обновления и удаления пользователей и обновления их балансов
Используя библиотеку `requests`, напишите функцию `fetch_weather(city)`, которая принимает на вход название города и возвращает текущую температуру в этом городе. Используйте любое открытое API для получения данных о погоде. Важно, вы можете использовать погрешность, температура меняется не чаще 10 минут
Написать route для обновления баланса пользователя, как в большую, так и в меньшую сторону на сумму равную температуре воздуха в выбранном городе, принимающего параметры userId, city.
Важным условием является то, что баланс пользователя не может быть отрицательным.
Изменение баланса должно производиться в реальном времени, без использования очередей и отложенных задач.

Выполнено:
1) Каждый раз при запуске файла app.py в БД создаются ещё 5 пользователей с указанным балансом
2) Баланс пользователя обновляется в зависимости от погоды в выбранном городе
   
Что бы запустить проект нужно:
  1) Настроить виртуальное окружение
  2) Устанавливаем зависимости выполнив команду (pip install -r requirements.txt)
  3) Переходим по ссылке http://127.0.0.1:5000
  4) Всё готово - тестируйте
