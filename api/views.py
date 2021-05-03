from django.shortcuts import render
from django.http import HttpResponse
from . import scrape

# Create your views here.
def foo(req):
    start=req.GET['start']
    end=req.GET['end']
    timing=req.GET['time']
    result=scrape.routes(start,end,timing)

    
    return HttpResponse(result)