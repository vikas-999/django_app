from django.shortcuts import render

# Create your views here.
def forvw(request):
    a = [1,2,3,4,5,6,7,8]
    e = [2,4,6,8]
    context = {"a":a, "e":e}
    return render(request,"for.html",context)

data = [
        {"name":"vikas","mob":3203397819,"gmail":"vikas.com"},
        {"name":"ram","mob":30290198100,"gmail":"hakaak.com"},
        {"name":"mama","mob":3301920190,"gmail":"mama.com"},
]

def for1(request):
    context = {"data":data}
    return render(request,"for2.html",context)

def filtervw(request):
    context = {'data':"python is easy","d1":"HELLO ANNA","d2":"jakesully", "l":["python","webtech","sql","django"],
                'data3':"pyspiders ", "l3":range(1,21)
                }

    return render(request,"filter.html",context)