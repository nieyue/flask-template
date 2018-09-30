#-*- coding: utf-8 -*-
import json
class Result():
    """
    获取对象的json
    """
    def getJson(User):
        return json.dumps(User,ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        #return json.dumps(Object,ensure_ascii=False)
    # def __init__(self, code,msg,list):
    #     self.code = code
    #     self.msg = msg
    #     self.list = list
    def getResult(code,msg,list=''):
        data={}
        data['code']=code
        data['msg']=msg
        data['list']=list
        return json.dumps(data,ensure_ascii=False)#ensure_ascii防止中文ascii编码