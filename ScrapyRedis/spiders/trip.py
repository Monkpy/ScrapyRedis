# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy_redis.spiders import RedisSpider

from ScrapyRedis.items import ScrapyredisItem


class TripSpider(RedisSpider):
	name = 'trip'
	allowed_domains = ['www.tripadvisor.cn']
	redis_key = 'trip:start_urls'

	def parse(self, response):
		for i in range(1, 2):  # 11
			if i == 1:
				url = 'http://www.tripadvisor.cn/Attractions-g297463-Activities-Chengdu_Sichuan.html'
			else:
				page = (i-1)*30
				url = 'https://www.tripadvisor.cn/Attractions-g297463-Activities-oa{}-Chengdu_Sichuan.html#FILTERED_LIST'.format(page)
			yield scrapy.Request(url, callback=self.parse_links)

	def parse_links(self, response):
		url_links = response.xpath('//div[@id="FILTERED_LIST"]/div/div/div/div/div[1]/a/@href').extract()
		for link in url_links:
			url_new = 'https://www.tripadvisor.cn' + link
			yield scrapy.Request(url_new, callback=self.parse_cont)

	def parse_cont(self, response):
		item = ScrapyredisItem()
		item['link'] = response.url
		title = response.xpath('//h1[@id="HEADING"]/text()').extract_first()
		if title:
			item['name'] = title
		else:
			item['name'] = ''
		en_title = response.xpath('//h1[@id="HEADING"]/div/text()').extract_first()
		if en_title:
			item['en_name'] = en_title
		else:
			item['en_name'] = ''
		opentime = ''.join(response.xpath('//span[@class="is-hidden-mobile header_detail"]//text()').extract())
		if opentime:
			item['opentime'] = opentime.strip()
		else:
			item['opentime'] = opentime
		add = ''.join(response.xpath('//div[@class="is-hidden-mobile blEntry address  ui_link"]/span[2]//text()').extract())
		add2 = ''.join(response.xpath('//div[@class="is-hidden-mobile blEntry address  ui_link showBizHour"]/span[2]//text()').extract())
		if add:
			item['address'] = add
		else:
			if add2:
				item['address'] = add2
			else:
				item['address'] = ''
		pthoto = response.xpath('//*[@id="taplc_resp_photo_mosaic_ar_responsive_0"]/div/div[4]/div[1]/div[1]/div/img/@data-lazyurl').extract_first()
		if pthoto:
			item['photo'] = pthoto
		else:
			item['photo'] = ''
		try:
			intro = re.findall(r'description":"(.*?)"', response.text, re.S)
			if intro:
				item['intro'] = intro[0].encode().decode('unicode_escape')
			else:
				item['intro'] = '暂无描述...'
		except:
			item['intro'] = ''
		comment = response.xpath('//div[@class="listContainer hide-more-mobile"]//p[@class="partial_entry"]/text()').extract()
		x = {}
		if comment:
			for i, com in enumerate(comment):
				x[i] = com.replace('\n', '')
				item['comment'] = str(x)
		else:
			item['comment'] = '暂无评论...'
		yield item






