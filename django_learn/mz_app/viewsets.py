from mz_app.serializers import PersonSerializer
from mz_app.models import Person

from dynamic_rest.viewsets import DynamicModelViewSet

class PersonViewSet(DynamicModelViewSet):
    """
    Persons API.
    """
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
