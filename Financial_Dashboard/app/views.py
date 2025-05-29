from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
from datetime import datetime


def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context=None, request=request))


def current_time(request):
    now = datetime.now()
    date_format = now.strftime('%d-%m-%Y %H:%M:%S')
    return HttpResponse(date_format)


def workdir(request):
    contents = os.listdir()
    res = '\n'.join(contents)
    return HttpResponse(res, content_type=r'text\plain; charset=utf-8')
