# -*- coding: utf-8 -*-
# filename: material.py
import urllib2
import json

from basic import Basic

class Material(object):
    #上传图文
    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib2.urlopen(postUrl, news)
        print urlResp.read()

if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    news =(
    {
        "articles":
        [
            {
            "title": "test",
            "thumb_media_id": "X2UMe5WdDJSS2AS6BQkhTw9raS0pBdpv8wMZ9NnEzns",
            "author": "vickey",
            "digest": "",
            "show_cover_pic": 1,
            "content": "<p><img src="" alt="" data-width="null" data-ratio="NaN"><br  /><img src="" alt="" data-width="null" data-ratio="NaN"><br  /></p>",
            "content_source_url": "",
            }
        ]
    })
    #news 是个dict类型，可通过下面方式修改内容
    #news['articles'][0]['title'] = u"测试".encode('utf-8')
    #print news['articles'][0]['title']
    news = json.dumps(news, ensure_ascii=False)
    myMaterial.add_news(accessToken, news)