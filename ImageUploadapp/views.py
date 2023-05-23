from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .forms import ImageForm
from django.db.models import Q
from .models import Images
from django.core.files.storage import FileSystemStorage
import base64
from PIL import Image
import io
from django.conf import settings
from django.core.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)


def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Already Exist")
                logger.warning('Warning message')
                return redirect(register)
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                logger.debug('Debug message')
                return redirect('login_user')

    else:
        logger.warning('Warning message')
        return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            data = Images.objects.all()
            context = {
                'data': data
            }
            logger.info('Info message')
            return render(request, "display.html", context)

        else:
            messages.info(request, "Invalid Username or Password")
            logger.warning('Warning message')
            return redirect('login_user')
    else:
        logger.warning('Warning message')
        return render(request, "login.html")


def logout_user(request):
    auth.logout(request)
    logger.info('Info message')
    return redirect("login_user")


def upload(request):

    data = Images.objects.all()
    context = {
        'data': data,
    }

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form = Images()
            form.title = request.POST.get('title')
            form.description = request.POST.get('description')
            binaryimage = request.FILES['binaryimage']
            form.binaryimage = binaryimage.read()

            form.save()
            logger.debug('Debug message')
            return render(request, "display.html", context)

    else:
        form = ImageForm()
        logger.warning('Warning message')
        return render(request, 'upload.html', {'form': form})


def success(request):
    logger.info('Info message')
    return HttpResponse('successfully uploaded')


def display(request):
    data = Images.objects.all()

    context = {
        'data': data,
    }
    logger.info('Info message')
    return render(request, settings.IMGPATH, context)


def SearchImage(request):
    query = request.GET.get('q')
    images = Images.objects.filter(
        Q(image_file__icontains=query) | Q(title__icontains=query))
    context = {
        'data': images
    }
    logger.info('Info message')
    return render(request, "display.html", context)
