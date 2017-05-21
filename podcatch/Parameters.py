# ----------------------------------------------------------------------------
# pyPodCatch: Simple podcast fetching and tagging
# Copyright (c) 2016-2017 Jules Lallouette
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
import os
from configparser import SafeConfigParser
import pkg_resources
import appdirs

defaultMaxNbEpisodes = 10

cfgDir = appdirs.user_config_dir('podcatch')
if not os.path.exists(cfgDir):
    os.makedirs(cfgDir)
cfgFile = os.path.join(cfgDir, 'podcatch.conf')
lstFile = os.path.join(cfgDir, 'podcasts.list')
if not os.path.isfile(cfgFile):
    source = pkg_resources.resource_stream(__name__, 'config/podcatch.conf')
    with open(cfgFile, 'w') as dest:
        dest.writelines(source)
if not os.path.isfile(lstFile):
    source = pkg_resources.resource_stream(__name__, 'config/podcasts.list')
    with open(lstFile, 'w') as dest:
        dest.writelines(source)

paramParser = SafeConfigParser()
paramParser.read(cfgFile)

# General
podcastListPath = os.path.expanduser(str(paramParser.get('General', 'podcastListPath')))
if not os.path.isabs(podcastListPath):
	podcastListPath = os.path.join(cfgDir, podcastListPath)

defaultPodDirPath = os.path.expanduser(str(paramParser.get('General', 'defaultPodDirPath')))
defaultPodDirPath = defaultPodDirPath + ('' if defaultPodDirPath.endswith('/') else '/')
if not os.path.isabs(defaultPodDirPath):
	raise ValueError('The defaultPodDirPath parameter in ' + cfgFile + ' should be an absolute path.')

# Podcasts 
try:
	maxNbEpisodes = int(paramParser.get('Podcasts', 'maxNbEpisodes'))
except:
	maxNbEpisodes = defaultMaxNbEpisodes
	raise ValueError("Config error: maxNbEpisodes is not an integer (in " + cfgFile + ").")
defaultPodcastTitle = str(paramParser.get('Podcasts', 'defaultPodcastTitle'))
defaultPodcastAuthor = str(paramParser.get('Podcasts', 'defaultPodcastAuthor'))
defaultImgName = str(paramParser.get('Podcasts', 'defaultImgName'))

# Tagging
defaultGenre = str(paramParser.get('Tagging', 'defaultGenre'))

