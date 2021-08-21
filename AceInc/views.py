from AceInc.models import category
from django.shortcuts import render
from .models import blogpost, category,author,comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, JsonResponse
# Create your views here.


def categorypost(request):
    cat_data = category.objects.all()
    context = { "categories" : cat_data}
    return render(request, 'AceInc/home.html', context)

def home(request):
    posts =  blogpost.objects.all().order_by('-id')
    context = { "posts" : posts}
    return render(request, 'AceInc/all_post.html',context)

def CategoryView (request,cats):
    category = blogpost.objects.filter(blog_category =cats)
    return render(request, 'AceInc/categories.html', {'category': category})

def post_detail(request, id):
    post = blogpost.objects.get(id=id)
    com = comments.objects.filter(parent_post = id)
    auth = author.objects.all()
    context = { "com" : com , "post" : post , "auth": auth}
    print(auth)
    if request.method == "POST":
        commentname = request.POST["name"]
        commenttext = request.POST["comment"]
        print(commentname,commenttext)
        commitdata = comments(parent_post= post, name_data= commentname , comment_data = commenttext)
        commitdata.save()
    return render(request, 'AceInc/singlepost.html', context)

def search(request):
    term = request.GET.get("q", "")
    posts =  blogpost.objects.filter(title__contains=term)
    context = { "posts" : posts}
    return render(request, 'AceInc/home.html', context)

def authorview(request):
    authors = author.objects.all()
    context = { "authors" : authors}
    return render(request, 'AceInc/all_author.html', context)



@login_required(login_url='http://127.0.0.1:8000/admin/login/')
def secret_view(request):
    return JsonResponse(dict(a="sddffdfs", b="sjdbfksdjbfk"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def login_view(request):
    if request.method == "GET":
        msg = request.GET.get("msg")     
        context = {"msg" : msg}
        return render(request, 'AceInc/login.html', context)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponseRedirect(reverse('login') + "?msg=Please Enter Username and Password.")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login') + "?msg=It seems the credentials are incorrect,Plese try again!")

def aboutusview(request):
    return render(request, 'AceInc/aboutus.html')

def mail_view(request):
    return render(request, 'AceInc/mail.html')

