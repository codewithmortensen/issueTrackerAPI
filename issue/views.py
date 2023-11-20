from django.shortcuts import render
from django.http import HttpResponse


def issue(request):
    return HttpResponse('issues')
