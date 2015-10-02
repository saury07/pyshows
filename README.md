# pyshows

## Pre requirement

- Have an account on http://showrss.info
- Know you account id
  - Go to feeds
  - Generate a random feed
  - Find you id in generated url
- Have `pip` installed. See https://pip.pypa.io/en/stable/installing/

## Setup

### OSX

- Clone the repository
- Edit the script to setup your own id in the RSS feed url and the path you want files downloaded
- `pip install requests`
- `pip install xmltodict`
- If you want pyshows to automatically check for new shows, setup a cron running the script.
  - Example : `*/5 * * * * python /Users/toto/pyshows/pyseries.py` Will check every five minutes.

### Linux

Same as OSX, except the `open` command should be replaced by a bittorent client.

### Windows

No idea.

## Notes

- You probably do not want to delete torrents files, since it's used to know if a file has been downloaded
- Files are sorted on a per-show folder in the root you set in the script
- This script has been tested on a Macbook with Transmission client setup to not delete files, not to ask for anything on torrent opening and download files where the torrent is.
