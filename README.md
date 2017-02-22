# Podcatch
Podcatch is a simple podcast fetching tool made to be used with software like [gmusicbrowser](http://gmusicbrowser.org/), that are designed to handle large music libraries.
Podcatch treats podcasts as albums among an already existing music library; it downloads the last episodes, applies mp3 or FLAC tags, and downloads a front picture (if available) to be used by your music library software.

## Installation 
To install Podcatch, simply run:
```
sudo pip install podcatch
```

## How to use
Podcatch works with one or more files containing the podcasts you want to subscribe to.
Launching Podcatch without arguments will use the default podcast list.
```
podcatch
```
The first launch will tell you where the default podcast list is located (usually something like /home/user/.config/podcatch/podcasts.list).
If you want to launch Podcatch using a different list, you can either give it as argument or change the path to the default list (see the Configuration section).

### Podcast lists

A sample podcast list looks like this:
```
10 http://www.nycskeptics.org/storage/feeds/rs.xml
-1 http://feeds.nature.com/nature/podcast/current
```
Each line contains the number of most recent episodes you want to download (-1 for all episodes) and the URL of the rss feed.

### Fetching podcasts
podcatch goes through every podcasts in the list and downloads the appropriate number of new episodes to the default podcast directory (usually ~/Podcasts).
You can choose to download podcasts to several different directories by specifying their paths in the podcast list, like so:
```
/path/to/nature/podcasts
-1 http://feeds.nature.com/nature/podcast/current
15 http://feeds.nature.com/nature/podcast/neuropod
/path/to/nycskeptics/podcast
10 http://www.nycskeptics.org/storage/feeds/rs.xml
```
If no directories are provided in the podcast list, everything gets downloaded to the default directory specified in podcatch.conf.

### Configuration

The configuration file is in the same directory as the default podcast list (usually something like /home/user/.config/podcatch/podcatch.conf).
In this file, you can change the default podcast list, the default downloading directory, and other parameters. Each parameter is described there.

### Tagging
Podcatch also tags the downloaded episodes; in some cases, it might be useful to have some control over the content of the tag fields (title, genre, etc.).
You can replace the content of the tags by using regular expressions: you provide a regular expression that captures the content that you want to modify and the text that you want to replace it with.
For example, if you want to simplify the titles of a podcast, you can modify the corresponding podcast line in the following way:
```
10 http://www.nycskeptics.org/storage/feeds/rs.xml title "Rationally Speaking #[0-9]+ - (.*)" "\g<1>"
```
This will change the titles of the episodes from "Rationally Speaking #42 - Title of episode" to "Title of episode".
For each field that you want to modify, you need to supply 3 things: 
- the name of the field;
- the regular expression (enclosed by quotes) that will be matched by the field;
- the text to replace it with (enclosed by quotes).
In the example, we're modifying the title by capturing the beginning of all episodes (`Rationally Speaking #[0-9]+ - `) and then adding a group that captures everything else `(.*)`.
The new title only contains what the group contained, you can refer to groups by using `\g<1>`, replacing 1 by the group number.
The syntax is the same as what you would use with `re.sub(...)` in python (see the [documentation](https://docs.python.org/3.5/library/re.html#re.sub)).

Available fields are:
- albumartist
- artist
- title
- album
- tracknumber
- genre
- date

To modify several fields for one podcast, just chain them after the podcast URL in the podcast list.
