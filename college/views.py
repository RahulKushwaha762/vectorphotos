from django.shortcuts import render,HttpResponse,redirect
from .models import Images,Topics
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    category = ''
    val = ''
    if request.method == 'POST':
        category = request.POST['category']
        val = request.POST['op']
        if val == 'delete':
            Topics.objects.filter(name=category).delete()
            return redirect('/')
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

def delete(request,dl):
    deleteq = Images.objects.filter(id=dl).delete()
    return redirect('/')

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
        for i in all_topics:
            if i.name == name:
                error = 1
        if error == 0:
            topic.name = name
            topic.save()
        return redirect('/')
    context = {
            'error': error,
        }
    return render(request,'Newtopic.html',context=context)