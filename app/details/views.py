from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def details(request):
    context = {'title':'Список чертежей', 'content':'Список чертежей:', 'acln':['АЦЛН.005001.000.00','АЦЛН.005001.001.00','АЦЛН.005001.002.00']}
    return render(request, "details/info.html", context)

def number(request, specification):
    return HttpResponse(f"<h2>Перед вами новейшая разработка <br>{specification}</h2>")