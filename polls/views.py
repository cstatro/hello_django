from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('Welcome to the polls buddy!')


def details(request, question_id):
    return HttpResponse(f"You're looking at {question_id}.")
