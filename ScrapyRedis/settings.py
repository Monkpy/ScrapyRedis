# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyRedis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'ScrapyRedis'

SPIDER_MODULES = ['ScrapyRedis.spiders']
NEWSPIDER_MODULE = 'ScrapyRedis.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyRedis (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 3

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	"Accept-Language": "zh-CN,zh;q=0.9",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ScrapyRedis.middlewares.ScrapyredisSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
	# 'ScrapyRedis.middlewares.ScrapyredisDownloaderMiddleware': 543,
	# 'ScrapyRedis.middlewares.ProxyMiddleware': 543,  # IP代理中间件

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	'ScrapyRedis.pipelines.MongodbPipeline': 300,
	# 将爬取到的items保存到Redis 以便进行后续处理(注：值要小于上面的300才会将item数据存储到redis中)
	# 'scrapy_redis.pipelines.RedisPipeline': 100
}


# 调度器启用Redis存储Requests队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 确保所有的爬虫实例使用Redis进行重复过滤
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 将Requests队列持久化到Redis，可支持暂停或重启爬虫(断点续爬)
SCHEDULER_PERSIST = True

REDIS_URL = 'redis://root:密码@IP:6379'


DOWNLOAD_FAIL_ON_DATALOSS = False


# 设置的是防止空跑
MYEXT_ENABLED = True      # 开启扩展
IDLE_NUMBER = 10           # 配置空闲持续时间单位为 360个 ，一个时间单位为5s  (注：设置的数值是5的多少倍，持续空闲x倍)
EXTENSIONS = {
			'ScrapyRedis.extensions.RedisSpiderSmartIdleClosedExensions': 500,  # 注：需要在settings同级文件夹下创建extensions.py文件

		}

