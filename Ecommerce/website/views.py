from django.shortcuts import render
from models import Staff, Product

# Create your views here.
a = [
    {
        'name': 'Thiện Nhân',
        'age': 15
    },
    {
        'name': 'Quang Minh',
        'age': 14
    }
]

def home(req):
    product = Product.objects.all()
    return render(req, 'home.html', context={ 'data': a })

def signin(req):
    return render(req, 'signin.html')

def signup(req):
    return render(req, 'signup.html')