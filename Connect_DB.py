from dotenv import load_dotenv
import os
import psycopg2


class Connect_db:
    """Класс для подключения к Базе данных"""
    @staticmethod
    def connect_to_db():
        load_dotenv()
        postgres_key = os.getenv('PASSWORD_KEY')
        connection = psycopg2.connect(host='localhost', port=5432, dbname='course_work_5', user='postgres', password=postgres_key)

        cur = connection.cursor()

        return connection, cur


