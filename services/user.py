from typing import Union
from database.database import DB


class UserService:

    @staticmethod
    def initMe(username, firstname, lastname, faculty, year):
        DB.executemultiplesql([
            ('REPLACE INTO `user`(username, firstname, lastname, faculty, year) VALUES(?,?,?,?,?)',
             (username, firstname, lastname, faculty, year,)),
            ('REPLACE INTO self(username) VALUES (?)', (username,))
        ])

    @staticmethod
    def getProfile() -> tuple:
        username = DB.execute('SELECT * FROM self').fetchone()[0]
        return UserService.getUser(username)

    @staticmethod
    def isAdmin() -> boolean:
        return DB.execute('SELECT * FROM self LIMIT 1').fetchone()[1]

    @staticmethod
    def isMember() -> boolean:
        return DB.execute('SELCT * FROM self LIMIT 1').fetchone()[2]

    @staticmethod
    def updateProfile(firstname, lastname, faculty, year):
        username = UserService.getProfile()[0]
        DB.execute('UPDATE `user` SET firstname=?, lastname=?, faculty=?, year=? WHERE username=?',
                   (firstname, lastname, faculty, year, username))

    @staticmethod
    def getUser(username=None) -> Union[list, tuple]:
        users = []
        if(username is None):
            result = DB.execute('SELECT * FROM `user`')
            users = result.fetchall()
        else:
            result = DB.execute(
                'SELECT * FROM `user` WHERE username=? LIMIT 1', (username,))
            users = result.fetchone()
        return users

    @staticmethod
    def addUser(username, firstname, lastname, faculty, year, group_id='0'):
        DB.execute('INSERT INTO `user`(username, firstname, lastname, faculty, year, group_id) VALUES (?,?,?,?,?,?)',
                   (username, firstname, lastname, faculty, year, group_id))

    @staticmethod
    def updateGroup(username, newGroupID):
        DB.execute(
            'UPDATE `user` SET group_id=? WHERE username=?', (newGroupID, username,))

    @staticmethod
    def getAvailableUser() -> list:
        result = DB.execute(
            'SELECT username, firstname, lastname, faculty, year FROM `user` WHERE group_id="0"')
        return result.fetchall()