from django.shortcuts import render


# Create your views here.
def index(request): 
    return render(request, 'main/index.html')

def bio(request):
    return render(request, 'main/bio.html')  # Replace 'bio.html' with the actual template name

def code(request):
    return render(request, 'main/code.html')

def live(request):
    return render(request, 'main/live.html')

def build(request):
    return render(request, 'main/build.html')
