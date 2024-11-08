
from django.shortcuts import render
def home (request):
    images = [
        'main/img/person.png',
        'main/img/person.png',
        'main/img/person.png',
        'main/img/person.png',
        'main/img/person.png'
    ]
    return render(request,"main/mainpage.html",{'images': images})