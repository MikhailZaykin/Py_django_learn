from mz_app.serializers import PersonSerializer, GroupSerializer
from mz_app.models import Person, Group

from dynamic_rest.viewsets import DynamicModelViewSet

class PersonViewSet(DynamicModelViewSet):
    """
    Persons API.
    """
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GroupViewSet(DynamicModelViewSet):
    """
    Groups API.
    """
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
