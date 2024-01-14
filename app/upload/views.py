from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        image_name = '.'.join(image_url.split('.')[:-1]).split('/')[-1]
        return render(request, "upload.html", {
            "image_url": image_name
        })
    return render(request, "upload.html")
