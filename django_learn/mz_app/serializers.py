from mz_app.models import Person, Group

from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

class PersonSerializer(DynamicModelSerializer):
    class Meta:
        model = Person
        #name = 'person'
        fields = ('id', 'name', 'surname', 'patronymic', 'birth_day')


class GroupSerializer(DynamicModelSerializer):
    curator = DynamicRelationField(PersonSerializer, embed=True)

    class Meta:
        model = Group
        #name = 'group'
        fields = ('id', 'name', 'curator') 
