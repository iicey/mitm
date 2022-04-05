detail = Selector(response)

content = "\n\n".join(detail.xpath('//*[@id="js_content"]//text()').extract())
content = re.sub(r"\n+\s+", "\n\n", content)
pics = detail.xpath('//*[@id="js_content"]//img/@data-src').extract()
author = re.findall("var nickname = \"(.*?)\"", response.text)[0]
weixinId = detail.xpath('//*[@class="profile_meta_label"]'
                        '[contains(text(),"微信号")]/following-sibling::span/text()').extract_first()
aId = re.findall("var biz = \"(.*?)\"", response.text)[0]
article_time = re.findall("var ct = \"(.*?)\";", response.text)[0]
date = str(datetime.datetime.fromtimestamp(int(article_time)).strftime('%Y-%m-%d %H:%M:%S'))
