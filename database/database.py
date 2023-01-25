import mysql.connector as connector

class Database:
    def __init__(self) -> None:
        self.mydb = connector.connect(host='localhost',
                    user = 'root',
                    password='',
                    database = 'ClubManagementSystem',
                )

        quary = 'create table if not exists Clubmember(Name varchar(100), class varchar(100), studentID int primary key, batch varchar(10))'

        cursr = self.mydb.cursor()
        cursr.execute(quary)

    def insert_member(self, name, clss, student_id, batch):
        quary = f"insert into Clubmember(Name, class, studentID, batch) values('{name}', '{clss}', {student_id}, '{batch}')"
        # format(name, clss, student_id, batch)
        cursr = self.mydb.cursor()
        cursr.execute(quary)
        self.mydb.commit()

    def fech_data(self):
        quary = 'select * from Clubmember'
        cursr = self.mydb.cursor()
        cursr.execute(quary)
        return cursr

    def remove_member(self, student_id):
        query = "DELETE FROM clubmember WHERE studentID='{}'".format(student_id)
        cursr = self.mydb.cursor()
        cursr.execute(query)
        self.mydb.commit()
