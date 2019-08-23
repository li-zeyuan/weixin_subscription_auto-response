# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import random

import reply
import receive
import web

from content_test import CONTENT_TEST


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "lizeyuan" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志

            # 接收到的微信后台法发送过来的信息,调用parse_xml方法返回对象
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    # 被动回复文本信息
                    content = CONTENT_TEST[random.randint(0, 20)]
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    # 被动回复图片信息
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()

                else:
                    # 收到粉丝消息后不想或者不能5秒内回复时，需回复“success”字符串
                    return reply.Msg().send()
            elif isinstance(recMsg, receive.Event):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName

                if recMsg.MsgType == 'event':
                    # 关注/取消事件
                    content = "欢迎光临,请站稳了"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    # 收到粉丝消息后不想或者不能5秒内回复时，需回复“success”字符串
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment