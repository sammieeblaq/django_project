from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return render(request, "users/index.html")

def list(request):
    allUsers = User.objects.all()
    return render(request, "users/list.html", { "Users": allUsers })

def add(request):
    return render(request, "users/add.html")

def add_form_submission(request):
    print("Hello form is submitted")
    userName = request.POST["userName"]
    userEmail = request.POST["userEmail"]
    user = User(name=userName, email=userEmail)
    user.save()
    return render(request, "users/add.html")
