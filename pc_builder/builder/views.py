from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Build a PC!</h1>')

def about(request):
	return HttpResponse('<h1>About us</h1>')
# Create your views here.
