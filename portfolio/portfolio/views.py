#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:39:22 2020

@author: sbz
"""
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")
def about(request):
    return HttpResponse("This is our about page")
def contact(request):
    return HttpResponse("This is our contact page")

