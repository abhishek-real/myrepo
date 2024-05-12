from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse
from .models import databas
import time
# from django.db.models import Count
# Create your views here.
def home_page(request):
    
    if request.method == "POST" :
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        # print(user.first_name)
        
        if user is not None:
            print(user)
            login(request,user)
            fname=user.first_name
            print(fname)
            # return render(request,"word_search/page1.html",{'fname':fname})
            return redirect('paragraph')
        else:
            messages.error(request,"wrong credentials")
            return redirect('home')
    databas.objects.all().delete()
    logout(request)
    return render(request,"word_search/signin.html")


def register(request):
    if request.method == "POST" :
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        my_user = User.objects.create_user(username,email,pass1)
        my_user.first_name=fname
        my_user.last_name=lname
        my_user.save()
        messages.success(request,"your account has been succesfully created please login")
        return redirect(home_page)
    return render(request,"word_search/register.html")



def paragraph(request):
    if request.method == 'POST':
        text = request.POST['lines'].replace('\r\n', '\n')
        paragraphs_data = text.split('\n\n')
        i=0
        # print(paragraphs_data)
        for content in paragraphs_data:
            if len(content) == 0:
                continue
            i=i+1
            words = content.lower().split()
            for word in words:
                databas.objects.create(val1=word, val2=i)
                # print(i)
        return redirect('search_paragraph')
    if request.user.is_authenticated:
        return render(request,"word_search/page1.html")
    else:
        return redirect('home')
def search_paragraph(request):
    if request.method == 'POST':
        print("hello")
        search_input = request.POST['words'].strip()
        if search_input:
            paragraphs = databas.objects.filter(val1=search_input).distinct()
            # return JsonResponse({'paragraphs': list(paragraphs.values_list('val2', flat=True))})
            paragraphs =list(paragraphs.values_list('val2', flat=True))[0:10]
            ret ={
                'word' : search_input,
                'para' : paragraphs
            }
            return render(request,"word_search/page2.html",ret ) 
        else:
            return JsonResponse({'error': 'Search input is empty.'}, status=400)
    return render(request,"word_search/page2.html")
