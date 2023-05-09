import os
from audioop import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.db.models.signals import post_save
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect, redirect)
from django.template import loader

from cinema import settings
from .forms import FestivalForm, UploadForm
from .models import Footballer, Statistics, Profile, Item
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return render(request, 'base.html')


def search(request):
    name = request.GET.get("name", "")
    data = Footballer.objects.all().filter(name__contains=name).values()
    context = {
        'data': data,
        'name': name,
    }

    return render(request, "pages/search.html", context)


@permission_required('doctors.view_footballer', raise_exception=True)
def all(request):
    context = {
        "dataset": Footballer.objects.all()
    }

    return render(request, "pages/all.html", context)


def detail_view(request, id):
    context = {
        "data": Footballer.objects.get(id=id)
    }

    return render(request, "pages/detail_view.html", context)


def details(request, id):
    player = Footballer.objects.get(id=id)
    ans = Statistics.objects.filter(f_name=player.name).values()
    template = loader.get_template('pages/details.html')
    context = {
        'ans': ans,
        'player': player,
    }

    return HttpResponse(template.render(context, request))


@permission_required('doctors.add_statistics', raise_exception=True)
def create_view(request):
    context = {}
    form = FestivalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/all')
    context['form'] = form
    return render(request, "pages/create_view.html", context)


@permission_required('doctors.change_statistics', raise_exception=True)
def update_view(request, id):
    context = {}
    obj = get_object_or_404(Footballer, id=id)
    form = FestivalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/' + str(id))
    context["form"] = form

    return render(request, "pages/update_view.html", context)


@permission_required('doctors.delete_statistics', raise_exception=True)
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Footballer, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "pages/delete_view.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        check = ""

        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            check = "taken"
            context = {
                'check': check
            }
            return render(request, 'registration/signup.html', context)

        check = ""
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            check = "taken"
            context = {
                'check': check
            }
            return render(request, 'registration/signup.html', context)

        myuser = User.objects.create_user(username, email, pass1)
        profile.user = myuser
        profile.save()

        myuser.is_staff = True
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been signed up successfully!")
        return redirect('signin')

    return render(request, "registration/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Try again")
            return redirect('signin')

    return render(request, "registration/signin.html")


def signout(request):
    logout(request)
    return render(request, "registration/signout.html")


def profile(request):
    context = {}
    if request.method == 'POST' and request.FILES['myfile']:
        prod = Item()

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        profile.image = uploaded_file_url
        context["uploaded_file_url"] = profile.image
        prod.save()

    return render(request, 'pages/profile.html', context)


def addPhoto(request):
    if request.method == "POST":
        prod = Item()
        if len(request.FILES) != 0:
            prod.image = request.FILES['myfile']
        prod.save()
        messages.success(request, "Photo Added Successfully")
        return redirect('/')
    return render(request, 'pages/profile.html')



