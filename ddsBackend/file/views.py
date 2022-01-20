from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import myFile, ArchivedFile


# Create your views here.
# This upload view handle the upload files from the web app and use myFIle model.
def upload(request):
    context = {}
    if request.method == 'POST':
        index = request.POST['index']
        title = request.POST['title']
        author = request.POST['author']
        expiary_date = request.POST['expiary_date']
        files = request.FILES.getlist('document')
        is_lock = request.POST['is_lock']
        is_private = request.POST['is_private']
        user = request.user
        for file in files:
            myFile.objects.create(
                index=index,
                title=title,
                author=author,
                uploader=user,
                expiary_date=expiary_date,
                doc=file,
                is_private=is_private,
                is_lock=is_lock
            )
        return redirect('upload')
    return render(request, 'upload.html')


# This archive view handle the archived files from the web app and use ArchivedFIle model.
def archive(request, pk):
    if request.method == 'POST':
        file = myFile.objects.get(pk=pk)

        ArchivedFile.objects.create(
                index=file.index,
                title=file.title,
                author=file.author,
                uploader=file.uploader,
                expiary_date=file.expiary_date,
                doc=file.doc,
                is_private=file.is_private,
            )
        file.delete()
        return redirect("ddsHome")



