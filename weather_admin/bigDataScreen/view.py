from django.http import HttpResponse
import json
from . import default
import requests
def Users(request):
    print("hahahahhah")
    dict = {"name":"liushengbo","age":"22"}
    str = json.dumps(dict)
    resp=HttpResponse(str)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

def DataTr(request):
    data = default.GetWeather()
    dict = {"name":data}
    resp = HttpResponse(json.dumps(dict))

    resp['Access-Control-Allow-Origin'] = '*'
    return resp

def EstData(request):
    data = default.GetHighestTem()
    dict={"range":data}
    resp = HttpResponse(json.dumps(dict))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

def WeType(request):
    data = default.GetType()
    dict={"WeType":data}
    resp = HttpResponse(json.dumps(dict))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp
def LowTem(request):
    data = default.GetLowTem()
    dict={"LowTem":data}
    resp = HttpResponse(json.dumps(dict))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp
def feng(request):
    data = default.window()
    dict={"feng":data}
    resp = HttpResponse(json.dumps(dict))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp
def lastdata(request):
    data = default.lastData()
    dict = {"lastdata": data}
    resp = HttpResponse(json.dumps(dict))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp
