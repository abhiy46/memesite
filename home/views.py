from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
import requests
import logging
import json
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Welcome to meme site")

def meme(request):
    response = requests.get('https://api.imgflip.com/get_memes')
    urls =response.json()
    data=[]
    
    for meme in urls['data']['memes']:
        data.append(meme['url'])
    data=data[0:5]
    return render(request, 'home/meme.html',{'meme':data})





