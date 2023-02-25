from django.shortcuts import render
from django.http import HttpResponse
from Sportapp.forms import *
from Sportapp.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
# Create your views here.



def login(request):
    
    if request.method == "POST":

        form = AuthenticationForm(request,data = request.POST )

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            passwordtoken = form.cleaned_data.get("password")

            user = authenticate(username = usuario ,password = passwordtoken )

            if user:

                login(request,user)

                return render (request, "Sportapp/inicio.html" , {"message": f"welcome! {user}"})

        else:
            return render (request,"Sportapp/inicio.html" , {"message":"incorrect data"})
    else:

        form = AuthenticationForm()

    return render(request,"Sportapp/login.html" , {"formulario" : form})






def inicio(request):
    return render(request,"Sportapp/inicio.html")
    

def sport(request):  
    
    return render(request,"Sportapp/sportlive.html")


def player(request):
    play1 = Player(name= "Leonel", surname = "Messi", age = 35)
    play1.save()

    

    return render(request,"Sportapp/bestplayer.html")

def coach(request):
    trainer1 = Coach(name= "Lionel", surname = "Scaloni", age = 44, category = "profesional")
    trainer1.save()    

   

    return render(request,"Sportapp/bettertrainer.html")

def team(request):
    crew1 = Team(name = "River Plate", country = "Buenos Aires", host = "Monumental", Championships = 69)
    crew1.save()

    

    return render(request,"Sportapp/betterteam.html")


def sportFormulario(request):
    if request.method == "POST":
        formulario1 = sportFORMULARIO(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            sport = Sport(name= info["name"], country=info["country"])
            sport.save()
            return render(request, "Sportapp/inicio.html") 
            
    else:
        formulario1 = sportFORMULARIO()  

    return render (request, "Sportapp/sportForm.html", {"form1":formulario1 })  

def playerFormulario(request):
    if request.method == "POST":
        formulario2 = playerFORMULARIO(request.POST)
        if formulario2.is_valid():
            info1 = formulario2.cleaned_data
            player = Player(name = info1["name"],surname = info1["surname"], age = info1["age"])
            player.save()
            return render(request,"Sportapp/inicio.html")

    else:
        formulario2 = playerFORMULARIO()        
    
    return render(request,"Sportapp/playerForm.html", {"form2":formulario2})


def coachFormulario(request):
    if request.method == "POST":
        formulario3 = coachFORMULARIO(request.POST)
        if formulario3.is_valid():
            info2 = formulario3.cleaned_data
            coach = Coach(name = info2["name"] , surname = info2["surname"] , age = info2["age"] ,category= info2["category"])
            coach.save()
            return render (request,"Sportapp/inicio.html")

    else:
        formulario3 = coachFORMULARIO() 

    return render(request,"Sportapp/coachForm.html", {"form3":formulario3})          



 

def teamFormulario(request):
    if request.method == "POST":
        formulario4 = teamFORMULARIO(request.POST)
        if formulario4.is_valid():
            info3 =formulario4.cleaned_data
            team = Team(name = info3["name"], country = info3["country"], host = info3["host"], Championships = info3["Championships"])
            team.save()
            return render (request, "Sportapp/inicio.html")

    else:
        formulario4 = teamFORMULARIO()            

    return render (request,"Sportapp/teamform.html", {"form4" : formulario4})



def searchSport(request):
    return render(request,"Sportapp/inicio.html")


def result(request):
    if request.GET ["name"]:

        name = request.GET["name"]
        sports= Sport.objects.filter(name__iexact=name)

        return  render (request,"Sportapp/inicio.html", {"sports" :sports, "name":name })
        
    else:
        answer= "You didn't send data."

    return HttpResponse(answer) 


def readSport(request):

    sports = Sport.objects.all()

    contexto = {"deportes" : sports}

    return render (request, "Sportapp/readSports.html", contexto)


def createSport(request):

    if request.method == "POST":
        miform = sportFORMULARIO(request.POST)
        if miform.is_valid():
            infoA = miform.cleaned_data
            deporte = Sport(name=infoA["name"] ,country=infoA["country"])
            deporte.save()
            return render (request,"Sportapp/inicio.html")
        
    else:
        miform = sportFORMULARIO() 
    return render (request,"Sportapp/deporteformulario.html" , {"miform" : miform})



def eliminatesport(request, sportName):

    deporte = Sport.objects.get(name=sportName)  
    
    deporte.delete()

    deportes = Sport.objects.all()

    contexto= {"deportes": deportes}

    return render(request,"Sportapp/readSports.html" , contexto)



def editSport(request,sportName): 

    deporte = Sport.objects.get(name=sportName)

    if request.method == "POST":
        miform = sportFORMULARIO(request.POST)
        if miform.is_valid():
            infoA = miform.cleaned_data

            deporte.name = infoA["name"]
            deporte.country = infoA["country"]
            
            deporte.save()

            return render (request,"Sportapp/inicio.html")
        
    else:
        miform = sportFORMULARIO(initial= {"name" : deporte.name , "country" : deporte.country}) 
    return render (request,"Sportapp/editsport.html" , {"miform" : miform , "name": sportName})














    









        

        

   






    





