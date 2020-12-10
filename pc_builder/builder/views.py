from django.shortcuts import render
from django.http import HttpResponse


builds = [
	{
		'title':'build name here',
		'gpu':'RTX 3080',
		'cpu': 'Ryzen 9 3700x',		
	}
]


def home(request):
	context = {
		'builds': builds
	}
	return render(request, 'builder/home.html',context)

def login(request):
	return render(request, 'builder/login.html')
# Create your views here.
