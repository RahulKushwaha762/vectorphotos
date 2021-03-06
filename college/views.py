from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Images,Topics,Userdetails
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    message = 0
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        usermodel = auth.get_user_model()
        if User.objects.filter(email=email).exists():
            user = usermodel.objects.get(email=email)
            getusername = user.username
        else:
            getusername = ''

        user = auth.authenticate(username=getusername,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/index/")
        else:
            message = 1
    context = {
        'm':message,
    }
    return render(request,'login.html',context=context)

def register(request):
    message = 0
    userdetails = Userdetails()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                message = 2
            elif User.objects.filter(email=email).exists():
                message = 3
            else:
                user = User.objects.create_user(username=username,email=email,password=pass1)
                userdetails.emailw = email
                userdetails.passw = pass2
                userdetails.userw = username
                userdetails.save()
                user.save()
                print('user created')
                return redirect('/')
        else:
            message = 1
    context = {
        'm':message,
    }
    return render(request,'register.html',context=context)

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/")
def index(request):
    category = ''
    val = ''
    if request.method == 'POST':
        if 'category' in request.POST:
            category = request.POST['category']
        else:
            category = ''
        val = request.POST['op']
        if val == 'delete':
            Topics.objects.filter(name=category).delete()
            Images.objects.filter(topic=category).delete()
            return redirect('/index')
    img = Images.objects.all()
    topics = Topics.objects.all()
    f = 0
    user1 = auth.get_user(request)
    user = User.objects.get(username=user1.username)
    print(user.email)
    context = {
            'object':img,
            'topics': topics,
            'searched':category,
            'flag':f,
        }

    return render(request,'homepage.html',context=context)

def upload(request):
    return render(request,'selectupload.html')

def link(request):
    message = 0
    topics = Topics.objects.all()

    if request.method == 'POST':
        link = request.POST['linkimage']
        img = Images()
        if 'https://drive.google.com' in link:
            print("drive link=", link)
            split = link.split('/')
            print(split)
            img.link = 'https://drive.google.com/uc?id='+split[5]
        else:
            print("no drive link", link)
            img.link = link
        img.image = ''
        img.name = request.POST['filename']
        img.topic = request.POST['category']
        user1 = auth.get_user(request)
        user = User.objects.get(username=user1.username)
        img.email = user.email
        img.save()
        message = 1
    context = {
        'message': message,
        'topics': topics,
    }
    return render(request, 'link.html', context=context)

def linkpdf(request):
    message = 0
    topics = Topics.objects.all()
    if request.method == 'POST':
        link = request.POST['pdflink']
        img = Images()
        if 'https://drive.google.com' in link:
            print("drive link=", link)
            split = link.split('/')
            print(split)
            img.pdflink = 'https://docs.google.com/viewer?srcid='+split[5]+'&pid=explorer&efh=false&a=v&chrome=false&embedded=true'
        else:
            print("no drive link", link)
            img.pdflink = link
        img.image = ''
        img.link = ''
        img.name = request.POST['filename']
        img.topic = request.POST['category']
        user1 = auth.get_user(request)
        user = User.objects.get(username=user1.username)
        img.email = user.email
        img.save()
        message = 1
    context = {
        'message': message,
        'topics': topics,
    }
    return render(request, 'linkpdf.html', context=context)

def delete(request,dl):
    deleteq = Images.objects.filter(id=dl).delete()
    return redirect('/index')

def cdelete(request,cdl,topic):
    deleteq = Images.objects.filter(id=cdl).delete()
    return redirect('/selectcard/'+topic+'/')

def uploadimage(request):
    message = 0
    topics = Topics.objects.all()
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        url = fs.url(name)
        img = Images()
        img.image = name
        print("name = ",url)
        img.link = ''
        img.name = request.POST['filename']
        img.topic = request.POST['category']
        user1 = auth.get_user(request)
        user = User.objects.get(username=user1.username)
        img.email = user.email
        img.save()
        message = 1
    context = {
            'message':message,
            'topics':topics,
        }
    return render(request,'upload.html',context=context)

def newcat(request):
    error = 0
    if request.method == 'POST':
        topic = Topics()
        name = request.POST['category']
        all_topics = Topics.objects.all()
        user1 = auth.get_user(request)
        user = User.objects.get(username=user1.username)
        name = name.replace(" ","_")
        name = name.replace("&", "_and_")
        for i in all_topics:
            if i.name == name and user.email == i.temail:
                error = 1
        if error == 0:
            topic.name = name
            user1 = auth.get_user(request)
            user = User.objects.get(username=user1.username)
            topic.temail = user.email
            topic.save()
            error = 2
    context = {
            'error': error,
        }
    return render(request,'Newtopic.html',context=context)
@login_required(login_url="/")
def card(request):
    user1 = auth.get_user(request)
    user = User.objects.get(username=user1.username)
    count = Topics.objects.filter(temail=user.email).count()
    print(count)
    all_topics = Topics.objects.all()
    context = {
        'alltopics':all_topics,
        'count':count,
    }
    return render(request,'cards.html',context=context)
@login_required(login_url="/")
def selectcard(request,tp):
    category = tp
    img = Images.objects.all()
    topics = Topics.objects.all()
    f = 0
    context = {
        'object': img,
        'topics': topics,
        'searched': category,
        'flag': f,
    }
    return render(request, 'allimages.html', context=context)
