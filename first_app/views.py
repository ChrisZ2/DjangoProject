from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# make a map to assign the template value


def index(request):
    my_dict = {'insert_me': "Hello this is from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)
