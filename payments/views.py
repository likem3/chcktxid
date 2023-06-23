from rest_framework import generics
from payments.serializers import UserSerializer
from payments.models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSuspendView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'suspended'
        instance.save()
        return self.destroy(request, *args, **kwargs)