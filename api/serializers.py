from main.models import Animal, Contato
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id',
                  'foto',
                  'nome',
                  'idade',
                  'cidade_desaparecimento',
                  'estado_desaparecimento',
                  'status',
                  'informacoes_extras']


# Serializers define the API representation.
class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'animal']

    # necessario para tornar todos os campos necessários (required)
    def get_fields(self, *args, **kwargs):
        fields = super(ContatoSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "POST":
            fields['animal'].required = True
            fields['nome'].required = True
            fields['telefone'].required = True
        return fields
