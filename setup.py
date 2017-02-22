from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='podcatch',
    version='0.0.14',
    description='Podcast fetcher and tagger',
    url='https://github.com/jlallouette/PodCatch',
    author='Jules Lallouette',
    author_email='jules@lallouette.fr',
    license='GNU GPL v3',
    classifiers=[],
    keywords='podcast RSS download tagger',
    packages=['podcatch'],
    install_requires=['mutagen','feedparser','requests','tqdm','appdirs'],
    package_data={'podcatch': ['config/podcatch.conf', 'config/podcasts.list']},
    entry_points={
        'console_scripts': [
            'podcatch=podcatch.fetchPodcasts:main',
        ],
    },
)
