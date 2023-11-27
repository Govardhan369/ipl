from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
def virat(request):
    return render(request,'virat.html')

def siraj(request):
    return HttpResponse('<h1>Mia Bhai<h1>')

# Create your views here.
