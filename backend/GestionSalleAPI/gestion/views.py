from .serializer import SalleSerializer,FiliereSerializer,AttributionSerializer
from .models import Salle,Entite,Attribution
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import lancer_algo_affectation


# Create your views here.

"""CLASS GENERIQUE POUR LISTER LES SALLES """

class SalleReadAPI(generics.ListAPIView):
    queryset=Salle.objects.all()
    serializer_class=SalleSerializer
    
"""CLASS GENERIQUE POUR CRUD LES FILIERES""" 

class FiliereReadAPI(generics.ListAPIView):
    queryset=Entite.objects.all()
    serializer_class=FiliereSerializer
    
class FiliereCreateAPI(generics.CreateAPIView):
    queryset=Entite.objects.all()
    serializer_class=FiliereSerializer
    
    def get_serializer_context(self):
        # Ajouter la requête actuelle au contexte pour que le sérialiseur puisse y accéder
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
"""CLASS POUR LANCER L'ALGORITHME"""

class LancerAlgoAPI(APIView):
    def post(self, request):
        try:
            # Lancer l'algorithme et obtenir les attributions optimales
            attributions = lancer_algo_affectation()  # Fonction qui retourne les résultats de l'affectation

            # Sauvegarder les attributions dans la base de données
            for entite, salle in attributions.items():
                Attribution.objects.create(entite=entite, salle=salle)

            return Response(
                {"message": "L'algorithme a été exécuté avec succès et les salles ont été attribuées."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class AfficherAttribAPI(generics.ListAPIView):
    queryset=Attribution.objects.all()
    serializer_class=AttributionSerializer
    