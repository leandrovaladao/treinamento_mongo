from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from escola import models
from escola import serializers


class PersmissionsMixin(APIView):
    permission_classes = [IsAuthenticated]


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
