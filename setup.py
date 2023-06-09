
from setuptools import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name='tiktok_downloader',
  packages=['tiktok_downloader'],
  include_package_data=True,
  version='0.1.6',
  license='MIT',
  description='Tiktok Downloader&Scraper using bs4&requests',
  author='Sanzy Dev',
  author_email='hiisanzy@gmail.com',
  url='https://tiktok.sanzy.my.id',
  keywords=[
    'tiktok',
    'downloader',
    'scrapper',
    'tikdok-scraper',
    'tiktok-downloader'
  ],
  install_requires=[
          'bs4',
          'flask',
          'cloudscraper',
          'requests',
          'rich',
          'tqdm',
          'httpx',
          'aiohttp'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)
