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

```
[General]
# Path to the list of podcasts (relative to config directory or absolute)
podcastListPath = podcasts.list 
# Path to the default directory to which podcasts will be saved (absolute)
defaultPodDirPath = ~/Podcasts

[Podcasts]
# Maximum number of recent episodes to download when first adding the podcast (-1 to download all of them)
maxNbEpisodes = 15
# Default title in case of unspecified title
defaultPodcastTitle = Default Title
# Default name in case of unspecified authors
defaultPodcastAuthor = Unknown Author
# Saving name of the podcast image
defaultImgName = front

[Tagging]
# Genre field when tagging episodes
defaultGenre = Podcast
```

### Fetching
To fetch your podcasts, just run:
```
podcatch
```
