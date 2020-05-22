from django.conf.urls import url, include
from usuario.models import Dono
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class DonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dono
        fields = ['id', 'nome', 'email', 'telefone']

# ViewSets define the view behavior.
class DonoViewSet(viewsets.ModelViewSet):
    queryset = Dono.objects.all()
    serializer_class = DonoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'usuarios', DonoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    # url('api', include('rest_framework.urls', namespace='rest_framework'))
]
