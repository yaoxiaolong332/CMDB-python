# -*- coding:utf-8 -*-
import info_collection
#from conf import settings
import urllib,urllib2,sys,os,json,datetime
import api_token
import json

class ArgvHandler(object):
    def __init__(self,argv_list):
        self.argvs=argv_list
        self.parse_argv()

    def parse_argv(self):
        if len(self.argvs) >1:
            if hasattr(self,self.argvs[1]):
                func=getattr(self,self.argvs[1])
                func()
            else:
                self.help_msg()
        else:
            self.help_msg()
    def help_msg(self):
        msg = """
                collect_data
                run_forever
                get_asset_id
                report_asset
                """
        print msg
    def collect_data(self):
        obj=info_collection.Info_Collection()
        asset_data=obj.collect()
        a=file("C:\Users\YXL\Desktop\project\madking1\MadKingClient\data_json",'wb')
        json.dump(asset_data,a)
        a.close()
        print u"asset_data： "
        print asset_data
    def run_forever(self):
        pass
#    def __attach_token(self,url_str):
#        user=setting.Params['auth']['user']
#        token_id=setting.Params['auth']['token']
