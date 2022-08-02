import os
import psycopg2
import requests
import xml.etree.ElementTree as ET
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_valute():
    """
    Получение актуальной информации о курсе доллара к рублю
    """
    res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    res_xml = res.content
    tree = ET.fromstring(res_xml)
    for i in tree:
        if i.attrib.get('ID') == 'R01235':
            for j in i:
                if j.tag == 'Value':
                    return float(j.text.replace(',', '.'))
    return None


def create_db():
    """
    Создание базы данных
    """
    connection = psycopg2.connect(user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'),
                                  host=os.getenv('POSTGRES_HOST'), port=os.getenv('POSTGRES_PORT'))
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f'create database {os.getenv("POSTGRES_DB")}')
    cursor.close()
    connection.close()
