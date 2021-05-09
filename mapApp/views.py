from django.shortcuts import render

# Create your views here.
import urllib.request
import json
import time

def index(request):
    if request.method == 'POST':
        orig = request.POST['orig']
        dest = request.POST['dest']
       
        source = urllib.request.urlopen('http://www.mapquestapi.com/directions/v2/route?key=insertYourKey&from='+ orig +'&to='+ dest +'').read()
        list_of_data = json.loads(source)
        data ={
            "ToolRoad": str(list_of_data['route']['hasTollRoad']),
            "totalTime":str(list_of_data['route']['legs'][0]['formattedTime']),
            "miles": str(list_of_data['route']['distance']),
            "fuelUsed": str(list_of_data['route']['fuelUsed']),
            "kilometer":str("{:.2f}".format((list_of_data['route']['distance'])*1.60934)),
            "fuelLitre":str("{:.2f}".format((list_of_data['route']['fuelUsed'])*3.78541)),
            "orig": str(list_of_data['route']['locations'][0]['adminArea5'])+', '+str(list_of_data['route']['locations'][0]['adminArea3']),
            "dest": str(list_of_data['route']['locations'][1]['adminArea5'])+', '+str(list_of_data['route']['locations'][1]['adminArea3']),
            "move" :str(list_of_data["route"]["legs"][0]["maneuvers"])
        }
        
        print (data)
        move = list_of_data["route"]["legs"][0]["maneuvers"]
       
    else:
        data = {}
    return render(request,"main/index.html",{'data':data,'move':move})    
