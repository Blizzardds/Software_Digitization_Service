from dds.decorators import allowed_users
from django.shortcuts import render
from file.models import myFile, ArchivedFile
from file.filters import myFileFilter, ArchivedFileFilter
from userAccount import views
from django.contrib.auth.decorators import login_required


# To show all the information of a user in his/her home page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    user = request.user
    files = myFile.objects.filter(uploader=user)
    myFilter = myFileFilter(request.GET, queryset=files)
    files = myFilter.qs
    return render(request, "home.html", {'files': files, 'myFilter': myFilter})


# To show the recent file information of a user.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def recent(request):
    return render(request, 'recent.html')


# To show the all the file information of a user.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def myfiles(request):
    user = request.user
    files = myFile.objects.filter(uploader=user)
    return render(request, 'myfiles.html', {'files': files})


# To show the trashed file information of a user.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def trash(request):
    return render(request, 'trash.html')


# To show the shared file information of a user.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def shared(request):
    return render(request, 'shared.html')


# To show the archive file information of a user.
@login_required(login_url='login')
def archive(request):
    user = request.user
    files = ArchivedFile.objects.filter(uploader=user)
    myFilter = ArchivedFileFilter(request.GET, queryset=files)
    files = myFilter.qs
    return render(request,'archive.html',  {'files':files, 'myFilter':myFilter})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def publicfolder(request):
    return render(request, 'publicfolder.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def privatefolder(request):
    return render(request, 'privatefolder.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def publicrepo(request):
    files = myFile.objects.filter(is_private=False)
    myFilter = myFileFilter(request.GET, queryset=files)
    files = myFilter.qs
    return render(request, 'publicrepo.html', {'files': files, 'myFilter': myFilter})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def privaterepo(request):
    files = myFile.objects.filter(is_private=True)
    myFilter = myFileFilter(request.GET, queryset=files)
    files = myFilter.qs
    return render(request, 'privaterepo.html', {'files': files, 'myFilter': myFilter})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def settings(request):
    return render(request, 'settings.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def newgroup(request):
    return render(request, 'newgroup.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def help(request):
    return render(request, 'help.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def search(request):
    myFilter = myFileFilter()
    return render(request, search.html, {'myFilter': myFilter})
