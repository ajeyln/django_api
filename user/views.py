from wsgiref import validate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import user
from .forms import EmployeeRegistration
from .models import User

# To Add the data to database
def home(request):
    if request.method == "POST":
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    return render(request, "index.html", {'form':fm})

# To view current data in database
def view(request):
    emply = User.objects.all()
    return render(request, "view_data.html", {'empl': emply})

# To update/edit the datas in database
def update(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)        
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
    return render(request, "update.html", {'form':fm})

# To delete the data in databse
def delete(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')