from django.shortcuts import render


# Create your views here.
def HomePage(request):
    return render(request, "HomePage.html")

def Dash(request):
    return render(request, "dashboard/dash.html")

def Census(request):
    return render(request, "dashboard/census.html")

