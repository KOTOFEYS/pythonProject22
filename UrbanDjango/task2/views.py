from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index_function(requests):
    return render(requests,'index_function.html')

class ClassIndex(TemplateView):
    template_name = 'index_class.html'

