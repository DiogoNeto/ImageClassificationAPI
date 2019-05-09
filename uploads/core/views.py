from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from django.http import JsonResponse

def home(request):
    
    #documents = Document.objects.all()

    #return render(request, 'core/home.html', { 'documents': documents })
    return render(request, 'core/home.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            gender = form.cleaned_data.get("gender")
            age = form.cleaned_data.get("age")
            form.save()
            return JsonResponse({'gender': gender , 'age': age })
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def simple_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return JsonResponse({'uploaded'})
    else:
        form = DocumentForm()
    return render(request, 'core/simple_upload.html', {
        'form': form
    })


