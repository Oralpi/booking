import pymysql as pyms


# class mysql:
#     def __init__(self):
#         self.db = self.call_of_connection()

#     def call_of_connection(self):
#         db = pyms.connect(host='', port=, user='',
#                           passwd='', db='', charset='utf8')

#         return db

#     def getDB(self):
#         return self.db


class pymsl():
    def __init__(self):
        print("생성!")
        self.db = pyms.connect(host='', port=, user='', passwd='',
                               db='', charset='utf8')

    def execute_selectAll(self, sql):
        db = self.db
        cur = db.cursor()
        cur.execute(sql)
        data = list(cur.fetchall())

        return data

    def execute_selectAllData(self, sql, data):
        db = self.db
        cur = db.cursor()
        cur.execute(sql, data)
        data = list(cur.fetchall())

        return data

    def execute_selectOne(self, sql):
        db = self.db
        cur = db.cursor()
        cur.execute(sql)
        res = list(cur.fetchone())

        return res

    def execute_selectOneData(self, sql, data):
        db = self.db
        cur = db.cursor()
        cur.execute(sql, data)
        res = list(cur.fetchone())

        return res

    def execute_commit(self, sql, data):
        try:
            db = self.db
            cur = db.cursor()
            cur.execute(sql, data)
        except pyms.err.MySQLError as e:
            print(e)

    def excute_deleteAll(self, sql):
        try:
            db = self.db
            cur = db.cursor()
            cur.execute(sql)
        except pyms.err.MySQLError as e:
            print(e)

    def commit(self):
        db = self.db
        db.commit()

    def execute_rollback(self):
        db = self.db
        db.rollback()

    def close(self):
        db = self.db
        db.close()
