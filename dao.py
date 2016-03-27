__author__ = 'sachaaury'
import sqlite3


class DAO(object):

    def __init__(self):
        self.db_path = 'storage/shows.db'
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def run(self, request, parameters=None, commit=False):
        cursor = self.connection.cursor()
        if parameters is None:
            cursor.execute(request)
        else:
            cursor.execute(request, parameters)
        if commit:
            self.connection.commit()
