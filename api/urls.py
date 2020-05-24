from django.conf.urls import url, include
from main.models import Animal
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['foto',
                  'nome',
                  'idade',
                  'cidade_desaparecimento',
                  'estado_desaparecimento',
                  'status',
                  'informacoes_extras']

# ViewSets define the view behavior.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(status=1)
    serializer_class = AnimalSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'animais', AnimalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    # url('api', include('rest_framework.urls', namespace='rest_framework'))
]
