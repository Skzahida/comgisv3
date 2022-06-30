from django.shortcuts import render
from .models import User, Awc
from django.contrib.auth import authenticate, login, logout

# from dashboard.models import IndiaFinal1617BasicLatlong

# Create your views here.
def HomePage(request):
    return render(request, "HomePage.html")

def Dash(request):
    return render(request, "dashboard/dash.html")

def Census(request):
    return render(request, "dashboard/census.html")

def health(request):
    return render(request, "dashboard/health.html")

def healthv2(request):
    return render(request, "dashboard/healthv2.html")

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
    return render(request, "dashboard/urban.html")       


def rtp(request):
    # toilets = new_toilet.objects.all()
    # context = {'toilets':toilets}
    return render(request, "dashboard/rtp.html")    

def Tribal_Area_Maharashtra(request):
    return render(request, "dashboard/tdd.html")    

def map(request):
    return render(request, "dashboard/map.html") 

def chandrapurcfrgis(request):
    return render(request, "dashboard/chandrapurgis.html") 

def chandrapurruralgis(request):
    return render(request, "dashboard/chandrapurruralgis.html") 
    
def raigadgis(request):
    return render(request, "dashboard/raigadgis.html")       

user={'is_authenticated':FALSE}
# urban nutrition route
def urban_nutrition(request):
    data = Awc.objects.all()
    return render(request, "dashboard/urban_nutrition.html",{'title':'URBAN NUTRITION','user':user,'data':data})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(username=username, password=password)
        print(username,password,user)

        if user is not None:
            # if user.is_active: 
            login(request, user)
            request.session['username']=username
            request.session['role']=role
            # form = User(username, password,role)
            # messages.info(request,_(u"Logged in sucessfully."))
                # analytics = initialize_analyticsreporting()
                # response = get_report(analytics)
                # recd_response = print_response(response)
                # context = {
                #     'Visitor_count': recd_response
                # }

                # return render(request, "rating.html", context)
            return render(request,"dashboard/profile.html",{'title':'URBAN NUTRITION', 'user':request.session['username'], 'role':role})

    context = {}
    context['form']= User()
   
    return render(request, "dashboard/login.html",context)


def logoutUser(request):
    del request.session['username']
    logout(request)
    return render(request,"dashboard/urban_nutrition.html",{'title':'URBAN NUTRITION'})
# def schools(request):
#     school_states = IndiaFinal1617BasicLatlong.objects.values_list('states', flat=True).distinct().order_by('states')
#     context={'school_states': school_states}
#     return render(request, "dashboard/schools.html",context)     
def profile(request):
    user = request.session['username']
    return render(request, "dashboard/profile.html",{'user':request.session['username']})


# def schools(request):
#     school_states = IndiaFinal1617BasicLatlong.objects.values_list('states', flat=True).distinct().order_by('states')
#     context={'school_states': school_states}
#     return render(request, "dashboard/schools.html",context)     


