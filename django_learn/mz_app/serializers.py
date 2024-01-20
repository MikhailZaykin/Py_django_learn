from mz_app.models import Person

from dynamic_rest.serializers import DynamicModelSerializer

class PersonSerializer(DynamicModelSerializer):
    class Meta:
        model = Person
        name = 'person'
        fields = ('id', 'name', 'surname', 'patronymic', 'birth_day')

