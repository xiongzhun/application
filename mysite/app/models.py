# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)

@python_2_unicode_compatible
class IDC(models.Model):
    name = models.CharField(u'机房', max_length=64)
    description = models.TextField(u'描述')
    contact = models.CharField(u'联系人', max_length=32)
    telphone = models.CharField(u'联系电话',max_length=32)
    address = models.CharField(u'地址',max_length=128)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机房"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Cabinet(models.Model):
    name = models.CharField(u'机柜', max_length=64)
    idc = models.ForeignKey(IDC, verbose_name="机房")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机柜"
        verbose_name_plural = verbose_name

@python_2_unicode_compatible
class Switch(models.Model):
    name = models.CharField(u'交换机', max_length=64)
    sn = models.CharField(u'资产编号', max_length=64, blank=True, null=True)
    up_port = models.CharField(u'汇聚接口', max_length=64, blank=True, null=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name = '机柜')
    ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"交换机"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class HostGroup(models.Model):

    name = models.CharField(u'组别', max_length=32)
    description = models.TextField(u'描述')

    class Meta:
        verbose_name = u"组别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Brand(models.Model):

    name = models.CharField(u'品牌', max_length=32)
    description = models.TextField(u'描述', blank=True, null=True)

    class Meta:
        verbose_name = u"品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Host(models.Model):
    idc = models.ForeignKey(IDC, verbose_name="机房")
    cabinet = models.ForeignKey(Cabinet, null=True, verbose_name="机柜")
    address_number = models.CharField(u"U位", max_length=32)
    name = models.CharField(u"SN", max_length=64)
    brand = models.ForeignKey(Brand, verbose_name="品牌", max_length=64, blank=True, null=True)
    model = models.CharField(u'类型', blank=True, null=True, max_length=64)
    ip = models.GenericIPAddressField(u'BMC IP', blank=True, null=True)
    mgr_ip = models.GenericIPAddressField(u'管理网IP',  blank=True, null=True)
    user = models.CharField(u'BMC 账户', max_length=64)
    password = models.CharField(u'BMC 密码', max_length=128)
    status = models.SmallIntegerField(u'服务器状态', choices=SERVER_STATUS, blank=True, null=True)
    host_group = models.ForeignKey(HostGroup, blank=True, null=True, verbose_name="组别")
    administrator = models.ForeignKey(AUTH_USER_MODEL, verbose_name="负责人")
    popurse = models.CharField(u'用途',  blank=True, null=True, max_length=128)
    info = models.CharField(u'环境信息',  blank=True, null=True,  max_length=128)
    left = models.IntegerField(u'剩余天数', null=True)
    guarantee_date = models.DateField(u'更新时间')
    cpu = models.CharField(u'CPU', max_length=64, blank=True, null=True)
    hard_disk = models.IntegerField(u'硬盘', blank=True, null=True)
    memory = models.IntegerField(u'内存', blank=True, null=True)

    system_user = models.CharField(u"系统账户", max_length=32, blank=True, null=True)
    system_password = models.CharField(u"系统账户密码", max_length=32, blank=True, null=True)
    description = models.TextField(u'描述', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"服务器"
        verbose_name_plural = verbose_name

    def profile(self):
        if len(str(self.info)) > 10:
            return '{}...'.format(str(self.info)[0:30])
        else:
            return str(self.info)
    profile.allow_tags = True


@python_2_unicode_compatible
class Port(models.Model):
    host = models.ForeignKey(Host)
    name = models.CharField(u"网卡编号", max_length=32, blank=True, null=True)
    switch_port = models.CharField(u"交换机端口", max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"网口信息"
        verbose_name_plural = verbose_name
