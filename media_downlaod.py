# -*- coding: utf-8 -*-
# filename: media.py
# 直接运行 media.py 即可把想要的素材下载下来，其中图文消息类型的，会直接在屏幕输出json数据段。
import urllib2
import json
from basic import Basic

class Media(object):
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()   #素材的二进制
            # 保存到本地的路径
            mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "get successful"
if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    mediaId = "_h-BUJFZT1KpEigH-hyzt3B0YNdxs-z2G3jNu5SWJwpdok6PvJuOsmzbhLZOXmRj"
    myMedia.get(accessToken, mediaId)