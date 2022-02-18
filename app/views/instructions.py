from app.forms import Service_net_useForm
from django.shortcuts import render
from django.http import FileResponse
from app.forms import *
from urgaz_tutorials.settings import BASE_DIR as dir
import os

def instructions(request):
    return render(request, 'views/instructions/instructions.html')

def group_outlook(request):
    return render(request, 'views/instructions/group_outlook.html')