#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import urllib2
import urllib
import json
import httplib
import simplejson
import sys

def send_msg(token,content,to_user="@all",to_party="@all",to_tag="@all",application_id=10,safe=0):
    try:
        data = {
           "touser": to_user,
           #"toparty": to_party,
           #"totag": 1,#to_tag
           "msgtype": "text",
           "agentid": application_id,
           "text": {
               "content": content,
           },
           "safe":safe
        }
        data = json.dumps(data,ensure_ascii=False)
        req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token))
        response = urllib2.urlopen(req,data)
        print response.read()
    except Exception,e:
        print str(e)


def get_token(CorpID="wx696d1a6b05e819d2",Secret="0LZzIhcl4ao1TK4UG6cnfK4sXS41GwyuSNUsSjSxkksFHceG-5BGQgYaa4QOs0OQ"):
    try:
        data = {
            "corpid":CorpID,
            "Secret":Secret
        }
        data = json.dumps(data,ensure_ascii=False)
        req=urllib2.Request("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(CorpID,Secret))
        response = urllib2.urlopen(req)
        decoded=json.loads(response.read())
        return decoded["access_token"]
    except Exception, e:
        print str(e)

#msg=sys.argv[1]
msg="test atom"
send_msg(get_token(),msg)
