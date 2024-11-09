
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

def page_not_f(request, exception):
    return render(request, 'main/ex404.html', {'message': 'Page not found'},status=404)
# if smth != smth
# raise Http404() or return redidect("home",permament=False)
# we can use a lot of filters in jinja2 "title|default : 'home' "