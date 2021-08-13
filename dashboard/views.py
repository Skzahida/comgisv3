from django.shortcuts import render


# Create your views here.
def HomePage(request):
    return render(request, "HomePage.html")

def Dash(request):
    return render(request, "dashboard/dash.html")

def Census(request):
    return render(request, "dashboard/census.html")

def health(request):
    return render(request, "dashboard/health.html")

def tdsc(request):
    return render(request, "dashboard/tdsc.html")

def tby(request):
    return render(request, "dashboard/tby.html")   

def deonadi(request):
    theme_name = 'Deonadi Project Dashboard'
    options = {
        '1' : 'Please Select Layers',
        '2' : 'Deonadi Watershed Drainage',
        '3' : 'Deonadi Watershed Villages',
        '4' : 'Deonadi Watershed Wells',
        '5' : 'Deonadi Watershed Landuse 2005-06',
        '6' : 'Deonadi Watershed Landuse 2011-12',
        '7' : 'Deonadi Watershed Soil Depth',
        '8' : 'Deonadi Watershed contour line'
    }
    return render(request, 'dashboard/deonadi.html', {'title' : theme_name, 'options' : options})

def pwss(request):
    return render(request, "dashboard/pwss.html")

def edu(request):
    return render(request, "dashboard/education.html") 


def urban_livability(request):
    return render(request, "dashboard/swm_opt-chk.html")       


def rtp(request):
    return render(request, "dashboard/rtp.html")    


