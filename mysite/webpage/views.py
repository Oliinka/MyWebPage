from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'webpage/index.html') #zadavam cestu ve webpage/templates - pages/main.html
