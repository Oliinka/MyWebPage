from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def bio(request):
    return render(request, 'main/bio.html')

def code(request):
    return render(request, 'main/code.html')

def build(request):
    return render(request, 'main/build.html')
    
def live(request):
    return render(request, 'main/live.html')

