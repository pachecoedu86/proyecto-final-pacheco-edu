from django.urls import path
from Sportapp.views import *



urlpatterns = [  
    path("", inicio, name= "Inicio"),  
    path("sportlive/", sport, name= "Sport"),
    path("bestplayer/", player, name= "Player"),
    path("bettertrainer/", coach,name= "Coach"),
    path("betterteam/" , team, name="Team"),
    path("formsport/",sportFormulario,name= "formulariosport"),
    path("formsplayer/",playerFormulario, name="formularioplayer"),
    path("formscoach/", coachFormulario, name = "formulariocoach" ),
    path("formsteam/", teamFormulario , name = "formularioteam"),
    path("searchSport/",searchSport,name= "SearchSport" ),
    path("results/", result, name = "searchResult"),
    path("iniciasesion/" , login, name = "Login"),

    #CRUD DE SPORTS
    path("readSPORTS/",readSport, name="SportsReads" ),
    path("createSPORTS/",createSport, name="Sportscreate" ),
    path("eliminateSPORTS/<sportName>/", eliminatesport, name= "Sporteliminate"),
    path("editarSPORTS/<sportName>/", editSport, name= "Sporteditar"),

]