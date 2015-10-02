# pyshows

## Pre requirement

- Have an account on http://showrss.info
- Know you account id
  - Go to feeds
  - Generate a random feed
  - Find you id in generated url
- Have `pip` installed. See https://pip.pypa.io/en/stable/installing/

## Setup

### OSX / Linux

- Clone the repository
- Edit the script to setup your own id in the RSS feed url and the path you want files downloaded
- `pip install requests`
- `pip install xmltodict`
- If you want pyshows to automatically check for new shows, setup a cron running the script.
  - Example : `*/5 * * * * python /Users/toto/pyshows/pyseries.py` Will check every five minutes.

### Windows

No idea.

## Notes

- You probably do not want to delete torrents files, since it's used to know if a file has been downloaded
- Files are sorted on a per-show folder in the root you set in the script
