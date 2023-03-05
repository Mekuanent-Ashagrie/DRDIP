from django.shortcuts import render
import requests
from capsule.models import launches, capsules

def home(request):
    return render(request, 'home.html', {})

def details(request):    
    capsuleList = capsules.objects.filter(cid=request.GET["cid"])
    launchList = launches.objects.filter(launch='5eb87ce1ffd86e000604b333')
    return render(request,'detail.html',{'capsuleList': capsuleList, 'launchList': launchList})

def getCapFromSpaceX(request):
    spaceXcapsules = (requests.get('https://api.spacexdata.com/v4/capsules')).json()
    return render(request, 'capsule.html', {'message': len(spaceXcapsules), 'capsuleList': spaceXcapsules})

def saveCapToDb(request):
    spaceXcapsules = (requests.get('https://api.spacexdata.com/v4/capsules')).json()
    # delete existing data ---- this is due to update_create method error 
    capsules.objects.all().delete()
    launches.objects.all().delete()
    for capsule in spaceXcapsules:
        # save capsules to sqlite table
        cap = capsules(reuse_count = capsule['reuse_count'], water_landings = capsule['water_landings'],
                        land_landings = capsule['land_landings'],last_update = capsule['last_update'], 
                        serial = capsule['serial'],status = capsule['status'], type = capsule['type'],
                        cid = capsule['id'])
        cap.save()
        for launch in capsule['launches']:
            lau = launches(cid = cap, launch=launch) 
            lau.save() #save set of launches to sqlite table

        # now get the data from database 
    capsuleList = capsules.objects.filter()
    return render(request, 'capsule.html', {'capsuleList': capsuleList})

def getCapFromDb(request):
    capsuleList = capsules.objects.filter()
    return render(request, 'capsule.html', {'capsuleList': capsuleList})



