# pyPodFetch
pyPodFetch is a simple podcast fetching tool made to be used with softwares like [gmusicbrowser](http://gmusicbrowser.org/), that are designed to handle large music libraries.
pyPodFetch treats podcasts as albums among an already existing music library; it downloads the last episodes, applies mp3 or FLAC tags, and downloads a front picture (if available) to be used by your music library software.

## Installation 
pyPodFetch depends on several other python libraries, to install them, run:
```
pip install mutagen feedparser pycurl
```
Then simply download pyPodFetch to any directory.

## How to use
pyPodFetch works with one or more files containing the podcasts you want to subscribe to.

### Podcast lists
A sample podcast file looks like this:
```
10 http://www.nycskeptics.org/storage/feeds/rs.xml
```
### Configuration
### Fetching
Simply run the fetching script:
```
python fetchPodcasts.py
```
