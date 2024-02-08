from django.shortcuts import render,redirect
from nasaapi import Client
from .models import store 

def landing(req):
	client = Client("Your_api_key")
	data = client.apod()
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

