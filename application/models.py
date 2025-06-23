from django.db import models
from django.contrib.auth.models import AbstractUser


class Area(models.Model):
    nome = models.CharField(max_length=100, help_text="Area Name in Itil")

    def __str__(self):
        return self.nome


class Proces(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Activitie(models.Model):
    nome = models.CharField(max_length=100, help_text="Activities in Itil")
    topico = models.ForeignKey(Proces, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Question(models.Model):
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Process = models.ForeignKey(Proces, on_delete=models.CASCADE)
    enunciado = models.TextField()
    alternativa_a = models.CharField(max_length=255)
    alternativa_b = models.CharField(max_length=255)
    alternativa_c = models.CharField(max_length=255)
    alternativa_d = models.CharField(max_length=255)
    alternativa_e = models.CharField(max_length=255)
    resposta_correta = models.CharField(
        max_length=1,
        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E")],
    )
    Activities1 = models.ForeignKey(
        Activitie,
        null=False,
        blank=False,
        related_name="activities1_questions",
        on_delete=models.CASCADE,
    )
    Activities2 = models.ForeignKey(
        Activitie,
        null=True,
        blank=True,
        related_name="activities2_questions",
        on_delete=models.CASCADE,
    )
    Activities3 = models.ForeignKey(
        Activitie,
        null=True,
        blank=True,
        related_name="activities3_questions",
        on_delete=models.CASCADE,
    )
    Activities4 = models.ForeignKey(
        Activitie,
        null=True,
        blank=True,
        related_name="activities4_questions",
        on_delete=models.CASCADE,
    )
    Activities5 = models.ForeignKey(
        Activitie,
        null=True,
        blank=True,
        related_name="activities5_questions",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.enunciado


class User(AbstractUser):
    ra = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome if self.nome else self.username
