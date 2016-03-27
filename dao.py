__author__ = 'sachaaury'
import sqlite3


class DAO(object):

    def __init__(self):
        self.db_path = 'storage/shows.db'
        self.connection = None
        self.connect()

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
        return cursor


class EpisodeDAO(DAO):

    def get_episode(self, show, season, number):
        request = """
                    SELECT * FROM Episode
                    WHERE show_name = ? AND season_number = ? AND episode_number = ?
                  """
        return self.run(request, (show, season, number)).fetchone()

    def save_episode(self, episode):
        request = """
                    INSERT INTO Episode VALUES (?,?,?,?,?,?,?)
                  """
        self.run(request, episode, commit=True)