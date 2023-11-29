from django.shortcuts import render

def ViewIndexPage(request):
    return render(request, 'homeApp/index.html')