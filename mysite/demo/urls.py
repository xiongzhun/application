# -*- coding: utf-8 -*-
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
from fibermotor import views as lib_mgr
xversion.register_models()


# from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^$', lib_mgr.host_listing),
    url(r'^host/(\d+)$', lib_mgr.host_detail, name='host-detail'),
    url(r'^host/unused/$', lib_mgr.host_unused),
    url(r'^host/no_time/$', lib_mgr.host_no_time),
    url(r'^host/out_time/$', lib_mgr.host_out_time),
    url(r'^host/active/$', lib_mgr.host_active),
]
