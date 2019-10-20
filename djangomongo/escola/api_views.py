from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from escola import models
from escola import serializers
from djangomongo.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class PersmissionsMixin(APIView):

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ProfessorViewset(viewsets.ModelViewSet, PersmissionsMixin):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer


class CursoViewset(viewsets.ModelViewSet, PersmissionsMixin):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


class AlunoViewset(viewsets.ModelViewSet, PersmissionsMixin):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializer


class UserViewset(viewsets.ModelViewSet, PersmissionsMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
