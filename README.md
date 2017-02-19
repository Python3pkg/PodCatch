# Podcatch
Podcatch is a simple podcast fetching tool made to be used with softwares like [gmusicbrowser](http://gmusicbrowser.org/), that are designed to handle large music libraries.
Podcatch treats podcasts as albums among an already existing music library; it downloads the last episodes, applies mp3 or FLAC tags, and downloads a front picture (if available) to be used by your music library software.

## Installation 
To install Podcatch, simply run:
```
pip install podcatch
```

## How to use
Podcatch works with one or more files containing the podcasts you want to subscribe to.

### Podcast lists
A sample podcast file looks like this:
```
10 http://www.nycskeptics.org/storage/feeds/rs.xml
```
### Configuration
### Fetching
Simply run the fetching script:
```
podcatch
```
