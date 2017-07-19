import json,os,platform,sys
from plugins import plugin_api

class Info_Collection(object):
    def __init__(self):
        pass
    def get_platform(self):
        os_platform=platform.system()
        return os_platform
    def collect(self):
        os_platform=self.get_platform()
        try:
            func=getattr(self,os_platform)
            info_data=func()
            formatted_data=self.build_report_data(info_data)
            #print formatted_data
            return formatted_data
        except AttributeError,e:
            sys.exit("Error:Madking doesn't support os [%s]!"  %os_platform)
    def Linux(self):
        sys_info=plugin_api.LinuxSysInfo()
        return sys_info
    def Windows(self):

        sys_info=plugin_api.WindowsSysInfo()
#        print sys_info
        return sys_info
    def build_report_data(self,data):
        return data
