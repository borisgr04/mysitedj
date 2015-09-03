import django as django
from django.shortcuts import render
from django.http import HttpResponse
from models import Question
from django.core import serializers
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def jsonExample(request):
    s = serializers.serialize('json',Question.objects.all())
    return HttpResponse(s, content_type="application/json")

'''
def jsonExample(request):
    s = serializers.serialize('json',Question.objects.all())
    return JsonResponse(s)
'''