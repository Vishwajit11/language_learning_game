from io import SEEK_CUR
import time
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.db.models import Sum
from django.contrib.auth.models import User, auth
from .models import TestResult
from .models import TestResult1
from .models import TestResult2
# from .models import TestResult21
# from .models import TestResult22
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
# from django.core.urlresolvers import resolve



from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"index.html")

def leaderboard(request):
    # Fetch all users with their total test scores
    users_with_scores = []
    users = User.objects.all()
    for user in users:
        test1e_score = TestResult.objects.filter(username=user.username, testname='test1e').aggregate(Sum('result'))['result__sum'] or 0
        test2e_score = TestResult1.objects.filter(username1=user.username, testname1='test2e').aggregate(Sum('result1'))['result1__sum'] or 0
        test3e_score = TestResult2.objects.filter(username2=user.username, testname2='test3e').aggregate(Sum('result2'))['result2__sum'] or 0
        total_score = test1e_score + test2e_score + test3e_score
        users_with_scores.append({'username': user.username, 'total_score': total_score})

    context = {'users_with_scores': users_with_scores}
    return render(request, 'leaderboard.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        password = request.POST.get("password")
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username'] = user.username 
            return redirect('MyApp:index')
        else:
            messages.info(request,'invalid credientials')
            return redirect('/login/')
    else:
        return render(request,"login.html")

def register(request):
    
    if request.method == 'POST': 
        if request.POST['username'] and request.POST['first_name'] and request.POST['email'] and request.POST['pass1'] and request.POST['pass2'] :
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2'] 
            if pass1 == pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'User already exists with that username.')
                    return redirect('MyApp:register')
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already registered')
                    return redirect('MyApp:register')


                else:
                    user = User.objects.create_user(username=username, password=pass1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    return redirect('MyApp:login')

            else:
                messages.info(request,'Password does not match')
                return redirect('MyApp:register')

        else:
            messages.info(request,"Invalid crediantials")
            return redirect('MyApp:register')
            
    else:
        return render(request,"register.html") 

def logout(request):
    auth.logout(request)
    return redirect("/")




def language(request):
  
    if request.session.get('username'):
        username = request.session['username']

        # Retrieve the user's test result for 'test1e'
        user_test_result = TestResult.objects.filter(username=username, testname='test1e').first()

        # Retrieve the user's test result for 'test2e'
        user_test_result1 = TestResult1.objects.filter(username1=username, testname1='test2e').first()

        user_test_result2 = TestResult2.objects.filter(username2=username, testname2='test3e').first()

        return render(request, "language.html", {'user_test_result': user_test_result, 'user_test_result1': user_test_result1, 'user_test_result2': user_test_result2})
    else:
        return render(request, "language.html")


@csrf_exempt
def test1e(request): 
    if request.method == 'POST':
        try:
            # Retrive the username and result from the post request sent from the frontend
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            result = data.get('result')
            testname = "test1e" 

            # Save the test results into database 
            test_result = TestResult(username=username, testname=testname, result=result)
            test_result.save_result()

            # To retrive the saved result fron the sqlite database use the follwing code
            
            queryset = TestResult.objects.filter(username=username) 
            # Serialize the QuerySet to JSON
            results = serialize('json', queryset)
            # Convert the serialized data to a Python dictionary 
            
            return JsonResponse({'message': 'Result saved successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    else:
        return render(request,"test1e.html")

@csrf_exempt
def test2e(request):
    if request.method == 'POST':
        try:
            # Retrive the username and result from the post request sent from the frontend
            data = json.loads(request.body.decode('utf-8'))
            username1 = data.get('username1')
            result1 = data.get('result1')
            testname1 = "test2e" 

            # Save the test results into database 
            test_result1 = TestResult1(username1=username1, testname1=testname1, result1=result1)
            test_result1.save_result1()

            # To retrive the saved result fron the sqlite database use the follwing code
            
            queryset = TestResult1.objects.filter(username1=username1) 
            # Serialize the QuerySet to JSON
            results = serialize('json', queryset)
            # Convert the serialized data to a Python dictionary 
            
            return JsonResponse({'message': 'Result saved successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    else:
        return render(request,"test2e.html")



@csrf_exempt
def test3e(request):
    if request.method == 'POST':
        try:
            # Retrive the username and result from the post request sent from the frontend
            data = json.loads(request.body.decode('utf-8'))
            username2 = data.get('username2')
            result2 = data.get('result2')
            testname2 = "test3e"

            # Save the test results into database 
            test_result2 = TestResult2(username2=username2, testname2=testname2, result2=result2)
            test_result2.save_result2()

            # To retrive the saved result fron the sqlite database use the follwing code
            
            queryset = TestResult2.objects.filter(username2=username2) 
            # Serialize the QuerySet to JSON
            results = serialize('json', queryset)
            # Convert the serialized data to a Python dictionary 
            
            return JsonResponse({'message': 'Result saved successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    else:
        return render(request,"test3e.html")




def languageh(request):
    return render(request,"languageh.html")


def test1h(request):
    # if request.method == 'POST':
    #     try:
    #         # Retrive the username and result from the post request sent from the frontend
    #         data = json.loads(request.body.decode('utf-8'))
    #         username21 = data.get('username21')
    #         result21 = data.get('result21')
    #         testname21 = "test1h"

    #         # Save the test results into database 
           
    #         test_result21 = TestResult21(username21=username21, testname21=testname21, result21=result21)
    #         test_result21.save_result21()

    #         # To retrive the saved result fron the sqlite database use the follwing code
            
    #         queryset = TestResult21.objects.filter(username21=username21) 
    #         # Serialize the QuerySet to JSON
    #         results = serialize('json', queryset)
    #         # Convert the serialized data to a Python dictionary 
            
    #         return JsonResponse({'message': 'Result saved successfully'})
    #     except json.JSONDecodeError as e:
    #         return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    # else:
        return render(request,"test1h.html")

def test2h(request):

    # if request.method == 'POST':
    #     try:
    #         # Retrive the username and result from the post request sent from the frontend
    #         data = json.loads(request.body.decode('utf-8'))
    #         username22 = data.get('username22')
    #         result22 = data.get('result22')
    #         testname22 = "test2h"

    #         # Save the test results into database 
           
    #         test_result22 = TestResult22(username22=username22, testname22=testname22, result22=result22)
    #         test_result22.save_result22()

    #         # To retrive the saved result fron the sqlite database use the follwing code
            
    #         queryset = TestResult22.objects.filter(username22=username22) 
    #         # Serialize the QuerySet to JSON
    #         results = serialize('json', queryset)
    #         # Convert the serialized data to a Python dictionary 
            
    #         return JsonResponse({'message': 'Result saved successfully'})
    #     except json.JSONDecodeError as e:
    #         return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    # else:
        return render(request,"test2h.html")
    

def test3h(request):
    return render(request,"test3h.html")


