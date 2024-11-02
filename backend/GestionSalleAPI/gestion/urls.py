from django.urls import path
from .views import FiliereCreateAPI,FiliereReadAPI,SalleReadAPI,LancerAlgoAPI,AfficherAttribAPI

urlpatterns = [
    path('list-salle',SalleReadAPI.as_view()),
    
    path('add-filiere',FiliereCreateAPI.as_view()),
    path('list-filiere',FiliereReadAPI.as_view()),
    
    path('lancer-algo/', LancerAlgoAPI.as_view(), name='lancer_algo'),
    
    path('attribution',AfficherAttribAPI.as_view()),
]
