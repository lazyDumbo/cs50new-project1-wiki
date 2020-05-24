from django.shortcuts import render, redirect
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request,title):
    entry=util.get_entry(title)
    if(entry):
        #write title.html and ParseHtml function
        return render(request,"encyclopedia/title.html",{'message':util.parseHtml(entry),'title':title})
    else:
        #write error.html
        return render(request,"encyclopedia/error.html",{'message': "title not found"}) 
def search(request):
    entry=util.Search(request.GET.get("q"))
    term=request.GET.get("q")
    return render(request, "encyclopedia/index.html", {
        "entries": entry,
        "message": f"Search results for {term}"
    })
def new(request):
    if request.method=='POST':
        title=request.POST.get("title")
        text=request.POST.get("text")
        entry=util.get_entry(title)
        if(entry):
            return render(request,"encyclopedia/error.html",{'message':"File with similar title alreay exists"})
        else:
            util.save_entry(title,text)
            return redirect(f'wiki/{title}')  
    else:
        return render(request,'encyclopedia/new.html')        
def edit(request,title):
    if request.method=='POST':
        title1=request.POST.get("title")
        text=request.POST.get("text")
        util.save_entry(title1,text)
        print(title)
        return redirect(f'/wiki/{title}')  
    else:
        ans=util.get_entry(title)
        #util.delete_entry(title)
        print(title)
        return render(request,'encyclopedia/edit.html',{'text':ans,'title':title}) 

def random1(request):
    x=util.list_entries()
    y=random.randrange(0,len(x)-1,1)
    return redirect(f'/wiki/{x[y]}')
