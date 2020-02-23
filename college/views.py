from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Images,Topics
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    message = 0
    if request.method == 'POST':
        password = request.POST['password']
        if password == '154321':
            message = 2
            return redirect("/index")
        else:
            message = 1
    context = {
        'm':message,
    }

    return render(request,'login.html',context=context)
def index(request):
    category = ''
    val = ''
    if request.method == 'POST':
        category = request.POST['category']
        val = request.POST['op']
        if val == 'delete':
            Topics.objects.filter(name=category).delete()
            Images.objects.filter(topic=category).delete()
            return redirect('/index')
    img = Images.objects.all()
    topics = Topics.objects.all()
    f = 0
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
        name = name.replace(" ","_")
        for i in all_topics:
            if i.name == name:
                error = 1
        if error == 0:
            topic.name = name
            topic.save()
            error = 2
    context = {
            'error': error,
        }
    return render(request,'Newtopic.html',context=context)

def card(request):
    all_topics = Topics.objects.all()
    context = {
        'alltopics':all_topics,
    }
    return render(request,'cards.html',context=context)
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
