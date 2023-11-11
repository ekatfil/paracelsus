from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User

# Create your views here.


def index(request):
    user = User.objects.all()
    content = {
        "title": "web",
        "users": user,
    }
    return render(request, "main/index.html", content)


def create_user(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.lastname = request.POST.get("lastname")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
    return HttpResponseRedirect("/")    
        

def edit(request, id):
    try:
        user = User.objects.get(id=id)
 
        if request.method == "POST":
            user.name = request.POST.get("name")
            user.lastname = request.POST.get("lastname")
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.save()
            return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")
    


def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")    
