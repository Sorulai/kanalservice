import time
from utils.db import OrderDb
from utils.google import get_google_add
from utils.services import get_valute, create_db
from dotenv import load_dotenv

dot_env = 'src/.env'
load_dotenv(dotenv_path=dot_env)


def main():
    """Главная функция, которая создает подключение к Google и БД,а так же получает данные о курсе"""
    # create_db()
    db = OrderDb()

    while True:
        value = get_google_add('test_list!A2:D')
        valute = get_valute()
        try:
            db.del_data()
        except Exception:
            pass
        db.add_data(value, valute)
        db.print_values()
        print('---------------')
        time.sleep(60)


if __name__ == '__main__':
    main()
