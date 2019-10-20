from django.db import models


class Pessoa(models.Model):

    class Meta:
        abstract = True

    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    cpf = models.BigIntegerField()
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)


class Professor(Pessoa):

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=45)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)


class Aluno(Pessoa):

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
