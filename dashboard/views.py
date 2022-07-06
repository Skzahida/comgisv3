# from asyncio.windows_events import NULL
# from operator import methodcaller
# from pickle import FALSE
# from subprocess import CREATE_NEW_CONSOLE
# from winreg import REG_DWORD_BIG_ENDIAN
from django.shortcuts import render,redirect
from .models import User, Awc
from django.contrib.auth import authenticate, login, logout
# from django.db import connection
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
    return render(request, "dashboard/urban.html",{'title':'URBAN LIVABILITY'})

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
# is_authenticated = false    
user={'is_authenticated':False}
# urban nutrition route
def urban_nutrition(request):
    # tt = Commgis.objects.all()
    # print(tt)
    # awc = list(Awc.objects.all())
    # cursor = connection.cursor()
    # cursor.execute("SELECT ST_X(geom) FROM awc1;")
    # lat = cursor.fetchall()
    # print( type (awc))
    # awc = [ i[13] for i in awc ]
    # awc = [ i[0] for i in awc ]
    # # x = slice()
    # l=''
    # awc = [ i[6:len(i)-1] for i in awc]
    # lat = [ i[0] for i in lat]
    # print(lat)
    # cursor.execute("SELECT ST_Y(geom) FROM awc1;")
    # lng = cursor.fetchall() 
    # lng = [ i[0] for i in lng]
    data = Awc.objects.all()
    # print(data)
    return render(request, "dashboard/urban_nutrition.html",{'title':'URBAN NUTRITION','data':data})     


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(username=username, password=password)
        # print(username,password,user)

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
            return redirect('profile')
            # return render(request,"profile",{'title':'URBAN NUTRITION', 'user':request.session['username'], 'role':role})

    context = {}
    context['form']= User()
   
    return render(request, "dashboard/login.html",context)


def logoutUser(request):
    del request.session['username']
    logout(request)
    return redirect("urban_nutrition")
    # return render(request,"dashboard/urban_nutrition.html",{'title':'URBAN NUTRITION'})
# def schools(request):
#     school_states = IndiaFinal1617BasicLatlong.objects.values_list('states', flat=True).distinct().order_by('states')
#     context={'school_states': school_states}
#     return render(request, "dashboard/schools.html",context)     
def profile(request):
    user = request.session['username']
    # print(user)
    data = Awc.objects.all().order_by('fid')
    return render(request, "dashboard/profile.html",{'user':user, 'role':request.session['role'],'data':data})

def aww_map(request):
    awc = Awc.objects.filter(fid=2)
    # print(awc[0].population)
    return render(request, "dashboard/aww_map.html",{'awc':awc[0]})
