from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):  # HTTPRequest
    return HttpResponse('Страница приложения women')


def categories(request, catid):  # HTTPRequest
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by category</h1><p>{catid}</p>')


def archive(request, year):  # HTTPRequest
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Articles by year</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')


