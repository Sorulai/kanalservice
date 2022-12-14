# kanalservice_test

Тестовое задание для Каналсервис. Скрипт получает данные из таблицы Google и записывает
эти данные в БД. Так же реализовано получение текущего курса доллара к рублю,
для конвертации валюты. Раз в минуту данные в БД обновляются параллельно 
своему текущему состоянию

[Google Sheet](https://docs.google.com/spreadsheets/d/1YJNeMjZHmX1rPmeLk2A2JY5Axq_OLeRw8zMHRp5DaNI/edit#gid=0)

***

## Запуск скрипта через Docker

Для запуска скрипта через докер, необходимо находится в директории __*kanalservice_test*__
Ввести команду в терминале:

`sudo docker-compose up --build
`

Когда контейнер будет готов, в терминале будут печататься данные из БД

***

## Запуск скрипта через терминал

### Утилиты которые понадобятся:
>Python
>
>PostgreSQL

### Подготовка для запуска:

1. Для начала необходимо заменить константы в файле .env 

- Для этого нужно перейти в __*kanalservice_test/src/*__ и в файле *.env*
заменить данные от PostgreSQL на свои и так же заменить POSTGRES_HOST на localhost(или на тот хост, где у вас находится БД)

- Файл .env должен выглядеть примерно вот так:

```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=test_db
POSTGRES_TABLE=test_table
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

2. Возвращаемся в директорию __*kanalservice_test*__ и в файле *main.py* на 13 строке 
раcкоментируем `create_db()`. Эта функция автоматически создаст БД в PostgreSQL.
3. Нужно создать виртуальное окружение и активировать его

- `python3 -m venv env `
- `source env/bin/activate `

4. Далее устанавливаем все зависимости из *requirements.txt*
- `pip install -r requirements.txt `

5. Запустить скрипт
- `python3 main.py`
