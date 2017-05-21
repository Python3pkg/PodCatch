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
from .Episode import *
from .Parameters import *
from .Utilities import *

import feedparser
import os
from os import mkdir, remove, path

tmpFeedFilePath = 'feed.xml'
epListFileName = 'episodes.dat'

class Podcast:
	def __init__(self, url, specifNbr = None, podcastDirPath = defaultPodDirPath):
		self.parser = None
		self.loadedFromFile = False
		if specifNbr:
			self.maxNbEpisodes = specifNbr
		else:
			self.maxNbEpisodes = maxNbEpisodes
		self.LoadXML(url)
		# Fill values
		if 'title' in self.parser.feed:
			self.title = self.parser.feed.title
		else:
			self.title = defaultPodcastTitle

		if 'author' in self.parser.feed:
			self.author = self.parser.feed.author
		else:
			self.author = defaultPodcastAuthor

		self.dirPath = podcastDirPath + self.title.replace('/', '_') + '/'
		try:
			os.makedirs(self.dirPath)
			print("Directory created")
		except OSError as ex:
			if not os.path.exists(self.dirPath):
				if os.path.exists(podcastDirPath):
					print(("Error, could not create: " + self.dirPath + ":" + str(ex)))
				else:
					print(("The podcast directory " + podcastDirPath + " does not exist."))
				raise

		try:
			if ('image' in self.parser.feed) and ('href' in self.parser.feed.image):
				self.imgURL = self.parser.feed.image['href']
			self.imgPath = self.dirPath + defaultImgName + '.' + self.imgURL.split('.')[-1]
			FetchFile(self.imgURL, self.imgPath)
		except:
			self.imgURL = ''

		self.episodes = []
		xmlEpisodes = self.parser.entries
		print((str(len(xmlEpisodes)) + " entries parsed."))
		# Load previously loaded episodes
		podFilePath = self.dirPath + epListFileName
		if os.path.exists(podFilePath):
			print(('Loading "' + podFilePath + '"...'))
			self.LoadEpisodesFromFile(self.dirPath + epListFileName)

		nbNewEp = 0
		for xmlEp in xmlEpisodes:
			# audio only - skip the videos
			for (ind, encl) in enumerate(xmlEp.enclosures):
				if ('type' in encl) and (encl['type'] == 'audio/mpeg'):
					ep = Episode(self, xmlEp, ind)
					if not ep.IsPresentIn(self.episodes):
						nbNewEp += 1
						self.episodes.append(ep)
		if nbNewEp == 0:
			print("No new episodes were published.")

		# Order by publication date
		self.OrderEpisodes()

		# If some episodes have already been fetched, fetch all the new ones
		if self.loadedFromFile:
			startInd = 0
			for (ind, ep) in enumerate(self.episodes):
				if ep.filePath != '':
					startInd = ind
					break
			if (startInd > len(self.episodes) - self.maxNbEpisodes) or (self.maxNbEpisodes == -1):
				startInd = max(0, len(self.episodes) - self.maxNbEpisodes) if self.maxNbEpisodes > -1 else 0
		# Otherwise, only fetch a limited number of episodes
		else:
			startInd = max(0, len(self.episodes) - self.maxNbEpisodes) if self.maxNbEpisodes > -1 else 0
		for ep in self.episodes[startInd:]:
			ep.FetchURL()

	def LoadXML(self, url):
		print(("Fetching " + url + " ..."))
		FetchFile(url, tmpFeedFilePath)
		print("Done.")
		try:
			self.parser = feedparser.parse(tmpFeedFilePath)
		except Exception as ex:
			print(("Couldn't parse " + url + ":" + str(ex)))
		os.remove(tmpFeedFilePath)

	def LoadEpisodesFromFile(self, filePath):
		epListFile = open(filePath, 'r')
		nbEp = int(epListFile.readline().strip('\n'))
		for i in range(nbEp):
			self.episodes.append(Episode(self))
			self.episodes[-1].LoadFromFile(epListFile)
		epListFile.close()
		self.loadedFromFile = True

	def SaveEpisodesToFile(self, filePath):
		epListFile = open(filePath, 'w')
		epListFile.write(str(len(self.episodes)) + '\n')
		for ep in self.episodes:
			ep.SaveToFile(epListFile)
		epListFile.close()
		
	def OrderEpisodes(self):
		self.episodes = sorted(self.episodes, key = lambda ep: ep.pubDate)
		for (num, ep) in enumerate(self.episodes, 1):
			ep.num = num

	def UpdateTags(self, filts=None):
		print("Updating tags...")
		nbUp = 0
		nbFailed = 0
		for ep in self.episodes:
			if ep.filePath != '':
				if not ep.UpdateTag(filts):
					nbFailed += 1
				nbUp += 1
		if nbFailed == 0:
			if nbUp > 0:
				print(("Tags from " + str(nbUp) + " files updated successfully."))
			else:
				print("No tags to update.")
		else:
			print((str(nbFailed) + "/" + str(nbUp) + " tags were not saved correctly."))

	def Save(self):
		self.SaveEpisodesToFile(self.dirPath + epListFileName)

