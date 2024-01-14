from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.template.defaulttags import comment
from .models import Draws
from .forms import DrawForm, SearchForm
import re


def index(request):
    context = {"buttions": ["Добавить", "Просмотр"], "Active": [0, 1]}
    return render(request, "details/base.html", context)


def load(request):
    dataset = QuerySet(Draws, "name")
    return details(request)


def details(request):
    context = {"title": "Список чертежей", "content": "Список чертежей:", "acln": []}
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            mask_name = request.POST['mask']
            acln = list(Draws.objects.filter(name__contains=mask_name))
        else:
            acln = list(Draws.objects.all())
    else:
        form = SearchForm()
        acln = acln = list(Draws.objects.all())
    context = {
        "title": "Список чертежей",
        "content": "Список чертежей:",
        "acln": acln,
        "form": form
    }
    return render(request, "details/info.html", context)


def number(request, specification):
    drw_obj = Draws.objects.get(name=specification)
    form = DrawForm(initial={'comment':drw_obj.comment})


    if request.method == "POST":
        drw_obj.comment = request.POST['comment']
        drw_obj.save()
        return redirect('details')
    form = DrawForm(initial={'comment':drw_obj.comment})        
    context = {
        
        "title": "Список чертежей",
        "content": specification,
        "acln": form
    }
    
    return render(request, "details/acln.html", context)


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        image_name = '.'.join(image_url.split('.')[:-1]).split('/')[-1]
        img_ext = image_url.split('.')[-1]
        if re.fullmatch(r'[0-9]{6}\.[0-9]{3}\.[0-9]{2}', image_name)and img_ext=='png':
           img_name = f'{image_name} is ok name'
           drw_obj, is_created = Draws.objects.get_or_create(name=image_name)
           drw_obj.save()
           
        else:
            image_name = f'Name Error: {image_name}'
               
        return render(request, "details/upload.html", {
            "image_url": img_name
        })

    return render(request, "details/upload.html")
