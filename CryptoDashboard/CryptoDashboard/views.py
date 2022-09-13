from django.http import HttpResponse,HttpResponseRedirect,request
from django.shortcuts import render
import requests
import json

def Dashboard(request):
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?"
      
    # requesting data from url
    data = requests.get(key)  
    data = data.json()

    return render(request,"Main.html",{"data":data})

def Crypto(request):
    # defining key/request url
    key = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
      
    # requesting data from url
    data = requests.get(key)  
    data = data.json()

    return render(request,"Crypto.html",{"data":data})