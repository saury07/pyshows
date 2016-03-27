from dao import DAO

__author__ = 'sachaaury'


class DBSchema(object):

    @staticmethod
    def bootstrap():
        requests = [
            """
              CREATE TABLE IF NOT EXISTS Episode(
                  id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                  show_name VARCHAR(255) NOT NULL,
                  season_number INTEGER DEFAULT NULL,
                  episode_number INTEGER DEFAULT NULL,
                  torrent_path VARCHAR(255) DEFAULT NULL,
                  downloaded_at DATE
              )
            """
        ]
        dao = DAO()
        dao.connect()
        for request in requests:
            dao.run(request, commit=True)

if __name__ == '__main__':
    DBSchema.bootstrap()

