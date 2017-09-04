#!/usr/bin/env python
# coding:utf-8
from models import Brand, Message, UserProfile, Job, Types, Test_report
import xadmin
# Register your models here.
from xadmin import views
from xadmin.views import ListAdminView


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True


class GlobalSetting(object):
    site_title = u"在线管理平台"
    site_footer = u"author 李振华"
    menu_style = "accordion"


class BrandAdmin(object):
    list_filter = ['name']
    list_display = ['name', 'create_time']
    search_fields = ['name', 'create_time']
    pass


class MessageAdmin(object):
    list_filter = ['brand', 'status']
    list_display = ['devices_id', 'name', 'version', 'brand', 'borrower', 'status', 'comment', 'modify_time', 'create_time']
    search_fields = ['devices_id', 'name', 'borrower__name']
    pass


class UserAdmin(object):
    list_filter = ['name']
    list_display = ['name', 'job_num', 'phone']
    search_fields = ['name', 'job_num']


class JobAdmin(object):
    list_filter = ['job_type', 'job_name',  'business_obj']
    list_display = ['job_type', 'job_name', 'work_time', 'business_obj',  'comment', 'create_time']
    search_fields = ['job_name']
    pass


class TypesAdmin(object):
    list_filter = ['name']
    list_display = ['name', 'create_time']
    search_fields = ['name']
    pass


class Test_reportAdmin(object):
    list_filter = ['name__name', 'test_type__name', 'test_name__job_name']
    list_display = ['name', 'test_name', 'test_type', 'test_time', 'comment', 'create_time']
    search_fields = ['name__name']


xadmin.site.register(Job, JobAdmin)
xadmin.site.register(Test_report, Test_reportAdmin)
xadmin.site.register(Types, TypesAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(UserProfile, UserAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
