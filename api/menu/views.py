# noinspection PyUnresolvedReferences,PyPackageRequirements
from menu.models import Week
# noinspection PyUnresolvedReferences,PyPackageRequirements
from menu.serializers import WeekSerializer
from rest_framework import viewsets


class WeekViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Week.objects.filter(user=user)
    serializer_class = WeekSerializer
    lookup_field = "num"
