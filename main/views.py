from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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
    


def edit_user(request, id):
    if request.method == "POST":
        user = get_object_or_404(User, id=id)
        user.name = request.POST.get("editName")
        user.lastname = request.POST.get("editLastname")
        user.email = request.POST.get("editEmail")
        user.save()
        return JsonResponse({'success': True})


def get_user_data(request, id):
    user = get_object_or_404(User, id=id)
    data = {
        'name': user.name,
        'lastname': user.lastname,
        'email': user.email,
    }
    return JsonResponse({'success': True, 'user': data})
   
    
    


def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")    
