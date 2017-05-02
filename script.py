from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler


google_crawler = GoogleImageCrawler('set directory location')
# example
# google_crawler = GoogleImageCrawler('C:\Python\image\Google')
google_crawler.crawl(keyword='Bed', offset=0, max_num=500,
                     date_min=None, date_max=None, feeder_thr_num=1,
                     parser_thr_num=1, downloader_thr_num=1,
                     min_size=(500,500), max_size=None)
