from django.shortcuts import render

# Create your views here.
def firstvw(request):
    return render(request,"first.html")

def ap1(request):
    context = {'data':1}
    return render(request,"ap1.html",context)

def two(request,pk,fk):
    context = {"pk": pk, "fk" : fk }
    return render(request,"two.html",context)

def compare(request,a,b):
    context = {"a":a,"b":b}
    return render(request,"compare.html",context)