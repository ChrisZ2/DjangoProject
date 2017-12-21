from django.shortcuts import render


# Create your views here.


def help(request):
    helpdict = {'help_inserts': 'Help page'}
    return render(request, 'appTwo/help.html', context=helpdict)
