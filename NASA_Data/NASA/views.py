from django.shortcuts import render,redirect
from nasaapi import Client
from .models import store 

def landing(req):
	client = Client("2BO6jqfHWtcS9JFbxYu4s4uTDPmGP81zreDakscg")
	data = client.apod()
	if not store.objects.filter(title=data['title']).exists():
		obj = store() 
		obj.title = data['title']
		obj.description = data['explanation']
		obj.url = data['url']
		
		obj.save()
	return redirect("/detail")

def allimage(req):
	detail = store.objects.all()
	print(detail)
	return render(req, "index.html", {"data": detail})
<<<<<<< HEAD
=======

>>>>>>> 888e0b0 (date added)
