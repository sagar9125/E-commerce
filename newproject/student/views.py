from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello django")
def blog(request):
    return render(request,'blog.html')