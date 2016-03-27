from dao import DAO

__author__ = 'sachaaury'


class DBSchema(object):

    def __init__(self):
        self.dao = DAO()

    @staticmethod
    def bootstrap():
        return [
            """
              CREATE TABLE IF NOT EXISTS Episode(
                  id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                  show_name VARCHAR(255) NOT NULL,
                  season_number INTEGER DEFAULT NULL,
                  episode_number INTEGER DEFAULT NULL,
                  torrent_path VARCHAR(255) DEFAULT NULL,
                  torrent_origin VARCHAR(255) DEFAULT NULL,
                  downloaded_at DATE
              )
            """
        ]

    @staticmethod
    def destroy():
        return [
            """
                DROP TABLE IF EXISTS Episode;
            """
        ]

    def execute(self, requests):
        for request in requests:
            self.dao.run(request, commit=True)

if __name__ == '__main__':
    schema = DBSchema()
    schema.execute(DBSchema.destroy())
    schema.execute(DBSchema.bootstrap())
