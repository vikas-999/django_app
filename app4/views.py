from django.shortcuts import render

# Create your views here.
def about(request,n,x):
    context = {'name':"st. cloud state university", 'location':'st cloud', "namee":n, "x":x}
    return render(request,"about.html",context)