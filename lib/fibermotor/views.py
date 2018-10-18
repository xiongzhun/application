# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from app import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your views here.

index_url = settings.PROJECT_ROOT


def host_listing(request):
    host_list = models.Host.objects.all().order_by("cabinet", "address_number")
    context = {
        'host_list': host_list,
        'index_url': index_url,

    }

    return render(request, 'host_list.html', context)


def host_detail(request, compter_id):
    try:
        p = models.Host.objects.get(id=compter_id)
        port_list = models.Port.objects.filter(host_id=compter_id)
        user_id = p.administrator_id
        cabint_id = p.cabinet_id
        switch = models.Switch.objects.filter(cabinet_id=cabint_id)
        user_name = User.objects.get(id=user_id)
    except models.Host.DoesNotExist:
        raise ("Computer does not exist")
    context = {
        'host_detail': p,
        'user_detail': user_name,
        'port_list': port_list,
        'switch_list': switch,
        'index_url': index_url,
    }
    return render(request, 'host_detail.html', context)


def host_unused(request):
    host_list = models.Host.objects.filter(popurse='无').order_by("cabinet", "address_number")
    context = {
        'host_list': host_list,
        'index_url': index_url,
    }

    return render(request, 'host_list.html', context)


def host_no_time(request):
    host_list = models.Host.objects.filter(~Q(popurse='无') & Q(left__gte=0) & Q(left__lt=15)).order_by("cabinet", "address_number")
    context = {
        'host_list': host_list,
        'index_url': index_url,
    }
    return render(request, 'host_list.html', context)


def host_out_time(request):
    host_list = models.Host.objects.filter(~Q(popurse='无') & Q(left__lt=0)).order_by("cabinet", "address_number")
    context = {
        'host_list': host_list,
        'index_url': index_url,
    }
    return render(request, 'host_list.html', context)


def host_active(request):
    host_list = models.Host.objects.filter(~Q(popurse='无') & Q(left__lt=0)).order_by("cabinet", "address_number")
    context = {
        'host_list': host_list,
        'index_url': index_url,
    }
    return render(request, 'host_list.html', context)

