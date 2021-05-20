# News-Archive Scraper

This script will crawl the page https://www.spiegel.de/international/

Entries will be saved on a local database on json format, **(db.json)**, to be easily accessed and manipulated anytime.

#### How to install

As there are no third parties tools to install, all you need is install python libraries and execute script.

Make sure to have python 3 installed, then execute the following commands to start:

```shell
python3 -m pip install -r requirements.txt
python3 main.py
```

#### Configuration (Optional)

Additionally you can change the scheduled crawling time.

To do so, open \*config.py\*\* and change the variable SCHEDULE to the value of minutes:

```python
SCHEDULE = 15 #For 15 minutes
```
