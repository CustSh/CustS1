from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def catalog (request):
    return render(request,"catalog/catalog.html")


def clickedProduct(request, article):
    template_name = f'article{article}.html'

    try:
        template = get_template(template_name)
    except TemplateDoesNotExist:
        raise Http404("Страница не найдена")

    return render(request, template_name)