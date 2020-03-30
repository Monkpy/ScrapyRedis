# scrapyRedis
scrapy-redis分布式
#  scrapy-redis分布式主要是在settings中添加3个配置，1.更换调度器2.更换去重规则3.配置redis连接
#  其次就是更换spider爬虫中的继承类，然后注释掉start_urls，使用redis_key='爬虫名:start_urls'
#  最后在启动爬虫后需往相应的redis中存入启动连接 lpush 爬虫名:start_urls http://xxxxxxxxx
  
  # 注：1.在写脚本时不能在使用dont_filter=True,这样会禁止去重，从而使redis中不会存储url链接的指纹从而不能达到去重的目的
  # 2.使用分布式后会出现调度空跑问题，故在settings里面设置了判断条件，从而实现自动停止运行完的脚本，可根据需求进行修改。
  # 3.一个小点，在写脚本使不能使用def start_request(self, spider)函数<也可能是开始的时候配置错误可以自行测试>
