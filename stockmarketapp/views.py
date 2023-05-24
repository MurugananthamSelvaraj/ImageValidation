from django.shortcuts import render
import requests
import json


def indexpage(request):

    if (request.method == 'POST'):
        # https = request.POST['https']
        # token = request.POST['token']
        api_request = requests.get(
            # https=token)
            "https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_64f3293b050744ebb5390a20c2ba3aeb")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error, data not loading"

    return render(request, 'index.html', {'api': api})


def stockdetailapicall(request):
    return render(request, 'stockdetailapicall.html')
