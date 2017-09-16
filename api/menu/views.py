# noinspection PyUnresolvedReferences,PyPackageRequirements
from menu.models import Week
# noinspection PyUnresolvedReferences,PyPackageRequirements
from menu.serializers import WeekSerializer
from rest_framework import viewsets


class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer
