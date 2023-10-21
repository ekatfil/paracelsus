from django.shortcuts import render

# Create your views here.


def index(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/index.html", content)
