from django.http import Http404
from rest_framework import viewsets, mixins, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User, Settings
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, SettingsSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


# noinspection PyMethodMayBeStatic
class SettingsView(views.APIView):
    def get_object(self, user):
        try:
            return Settings.objects.get(user=user)
        except Settings.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        settings = self.get_object(request.user)
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        if Settings.objects.filter(user=user).count() == 0:
            serializer = SettingsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            settings = Settings.objects.get(user=user)
            newSerializer = SettingsSerializer(data=request.data)
            if newSerializer.is_valid():
                settings.apikey = newSerializer.data['apikey']
                settings.project_name = newSerializer.data['project_name']
                settings.save()
                return Response(SettingsSerializer(settings).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        user = request.user
        Settings.objects.get(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
