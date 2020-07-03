from django.shortcuts import render,  HttpResponse, get_object_or_404, redirect,HttpResponseRedirect
from .models import author, catagory, article, comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import createForm ,RegisterUser, Public_author, comment_form, Create_catagory
from django.contrib import messages



# Create your views here.

def index(request):
    post = article.objects.all()
    search = request.GET.get('q')
    if search:
        post=post.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search)|
            Q(highlight__icontains=search)           
        )
    paginator = Paginator(post, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    all_page = paginator.get_page(page_number)
    content = {
        "post": all_page
        }
    return render(request, 'index.html', content)

def getauthor(request,name):
    post_author = get_object_or_404( User, username = name)
    auth = get_object_or_404(author, name = post_author.id)
    post = article.objects.filter(article_author = auth.id )
    paginator = Paginator(post, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    all_page = paginator.get_page(page_number)
    contex = {
        "post":all_page,
        "auth":auth,
    }
    return render(request, 'profile.html', contex)

def getsingle(request,id ):
    post = get_object_or_404(article, pk = id)
    first = article.objects.first()
    last = article.objects.last()
    getcomment = comment.objects.filter( post=id)
    related = article.objects.filter(catagory = post.catagory).exclude(id = id)[:4]
    form =comment_form(request.POST or None)
    if form.is_valid:
        instance =form.save(commit=False)
        instance.post=post
        instance.save()
        
    content = {
        "post": post,
        "first": first,
        "last": last,
        "related": related,
        "form": form,
        "comment":getcomment
        }
    return render(request, 'single.html', content)

def gettopic(request,name ):
    cat = get_object_or_404(catagory, name = name)
    post = article.objects.filter(catagory=cat.id ) 
    paginator = Paginator(post, 3) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    all_page = paginator.get_page(page_number)
    return render(request, 'catagory.html', {"post": all_page, "cat": cat })
    

def getlogin(request):
    if request.user.is_authenticated:
        
        return redirect('tube:index')
    else:
        if request.method== "POST":
            user =request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password = password)
            if auth is not None:
               login(request, auth)
               return redirect('tube:index') 
            else:
                messages.add_message(request, messages.ERROR, 'Password did not match ')
                return render(request, 'log.html')
    
    return render(request, 'log.html')
def getlogout(request):
    logout(request)
    return redirect('tube:index')


def getcreate(request):
    if request.user.is_authenticated:
        author_user = get_object_or_404(author, name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        contex ={"form":form}
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author= author_user
            instance.save()
            messages.success(request, 'Post Create Successfully Successfully ')
            return redirect('tube:index')
        return render(request, 'create.html', contex)
    else:
        return redirect('tube:loging')


def profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id= request.user.id )
        author_profile =author.objects.filter(name =user.id )
        if author_profile:
            authorUser = get_object_or_404(author, name = request.user.id )
            post = article.objects.filter(article_author =authorUser.id)
            return render(request, 'User.html', {'post': post, 'user': authorUser })
        else:
            form = Public_author(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name = user
                instance.save()
                return redirect('tube:profile')
            return render(request, 'creat_author.html', {"form": form})
                
    else:
        return redirect('tube:loging')

def update(request, id):
    if request.user.is_authenticated:
        author_user = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(article, id = id)
        form = createForm(request.POST or None, request.FILES or None, instance= post)
        contex ={"form":form}
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author= author_user
            instance.save()
            messages.success(request, 'Post updated Successfully ')
            return redirect('tube:profile')
        return render(request, 'create.html', contex)
    else:
        return redirect('tube:loging')

def delet(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(article, id = id)
        post.delete()
        messages.warning(request, 'Post Deleted Successfully ')
        return redirect('tube:profile')
    else:
        return redirect('tube:loging')


def register(request):
    form = RegisterUser(request.POST or None)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Deleted Successfully ')
        return redirect('tube:loging')
    return render(request, 'register.html', {'form':form})

def getsubjects(request):
    quary = catagory.objects.all()
    return render(request, 'subject.html',{"quary":quary})

def getcreate_topic(request):
    form = Create_catagory( request.POST or None )
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        return redirect('tube:Subject')
    return render(request, 'create_catagory.html', {"form":form})

'''def ok(request):
    return render(request, 'base.html')
    
def simple(request):
    return render(request, 'sample.html')
'''