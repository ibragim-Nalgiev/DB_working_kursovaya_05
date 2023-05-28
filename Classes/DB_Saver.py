from Connect_DB import Connect_db


class DB_Saver():

    def write_employers(self, data: list):
        """Записывает данные в таблицу employers"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                print('Начинаем вставку')
                cur.executemany("insert into employers (id, name, url, description) values (%s, %s, %s, %s)", data)
                connection.commit()
                print('Вставка завершена')
        connection.close()

    def write_vacancies(self, data: list):
        """Записывает данные в таблицу vacancy"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                print('Начинаем вставку')
                cur.executemany("insert into vacancy (id, name, salary_from, salary_to, emlployer_id, url, currency, requirement, responsibility) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                connection.commit()
                print('Вставка завершена')
        connection.close()

    def delete_employers(self):
        """Удаляет данные из таблицы employers"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from employers")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def delete_vacancy(self):
        """Удаляет данные из таблицы vacancy"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from vacancy")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def delete_all(self):
        """Удаляет данные из таблиц employers и vacancy"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from employers")
                cur.execute("delete from vacancy")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def read(self):
        """Чтение данных. Используется для тестов"""
        connection, cur = Connect_db.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                cur.execute("select * from employers")
                vac_info = cur.fetchone()
                print(vac_info)
        connection.close()




