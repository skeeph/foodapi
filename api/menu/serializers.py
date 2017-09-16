from rest_framework import serializers

# noinspection PyUnresolvedReferences,PyPackageRequirements
from menu.models import Week

from users.models import User


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ('num', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return Week.objects.create(user=user, **validated_data)