#!/usr/bin/python

import requests
import xmltodict
import re
import os


class RSSDownloader(object):

    def __init__(self):
        self.url = "http://showrss.info/rss.php?user_id=271870&hd=0&proper=1&magnets=false"

    def download(self):
        call = requests.get(self.url)
        return call.text

    def parse(self, text):
        data = xmltodict.parse(text)
        xml_items = data['rss']['channel']['item']
        parsed = []
        for xml_item in xml_items:
            print xml_item['title']
            regex = re.search('(.*) (\d+)x(\d)+', xml_item['title'])
            if regex is not None:
                parsed.append({
                    'show': regex.group(1),
                    'season': regex.group(2),
                    'episode': regex.group(3),
                    'torrent': xml_item['link']
                })
        return parsed


class TorrentDownloader(object):

    def __init__(self, episode_item):
        self.item = episode_item
        self.base_path = "/Users/sachaaury/Downloads/Series"

    def download(self):
        if not os.path.exists(self.base_path+'/'+self.item['show']):
            os.makedirs(self.base_path+'/'+self.item['show'])
        if os.path.exists(self.get_download_path()):
            return False
        torrent = requests.get(self.item['torrent'], stream=True)
        with open(self.get_download_path(), 'wb') as f:
            for chunk in torrent.iter_content(1024):
                f.write(chunk)
        return True

    def get_download_path(self):
        return "%s/%s/%sx%s.torrent" % (self.base_path, self.item['show'], self.item['season'], self.item['episode'])

    def open(self):
        path = TorrentDownloader.escape_path(self.get_download_path())
        command = 'open %s' % path
        os.system(command)

    @staticmethod
    def escape_path(path):
        return path.replace(' ', '\ ').replace('\'', '\\\'').replace('(', '\(').replace(')', '\)')


def main():
    downloader = RSSDownloader()
    items = downloader.parse(downloader.download())

    for item in items:
        t_downloader = TorrentDownloader(item)
        if t_downloader.download():
            t_downloader.open()

if __name__ == '__main__':
    main()
