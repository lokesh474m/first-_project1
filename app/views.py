from django.shortcuts import render
from django.http import *

def lokesh(request):
    return HttpResponse('<h1><marquee>Hai Baby are u fre now.</marquee>')
def baby(request):
    return HttpResponse('<h1><marquee>come fast kanna.Am waiting</marquee>')
