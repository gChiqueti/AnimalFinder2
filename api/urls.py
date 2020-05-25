from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Animal, Contato
from .serializers import AnimalSerializer, ContatoSerializer


class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Animal.objects.filter(status=1)
    serializer_class = AnimalSerializer

# ViewSets define the view behavior.
class ContatoViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = ContatoSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Contato.objects.filter(animal=username)

    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def update_contato(self, request, pk=None):
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            contato = Contato()
            contato.nome = request['nome']
            contato.telefone = request['telefone']
            contato.animal = request['animal']
            contato.save()
            return Response({'status': 'Contato adicionado'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'animais', AnimalViewSet)
router.register(r'contato/(?P<username>.+)', ContatoViewSet, basename='contato')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    # url('api', include('rest_framework.urls', namespace='rest_framework'))
]
