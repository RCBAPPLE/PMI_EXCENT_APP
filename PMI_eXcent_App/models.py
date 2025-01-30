from django.db import models
from django_mysql.models import ListCharField
from django.utils.timezone import now




class Diagnostic(models.Model):
    Client = models.CharField(max_length=100)
    SN_JacXson = models.CharField(max_length=20)
    Trigramme_Technicien = models.CharField(max_length=20)

    def __str__(self):
        return f"Diagnostic {self.Client}: technicien {self.Trigramme_Technicien}"


class Result(models.Model):
    Diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
    Partie = models.CharField(max_length=100, default = "Mise en sécurité")
    Question = models.CharField(max_length=100)
    Réponse = models.CharField(max_length=3)



class Template_Question(models.Model):
    id_question = models.CharField(max_length=10)  # Peut être '1', '1.0', etc.
    question_texte_FR = models.TextField( default="")  # Texte de la question en francais sur la page
    question_texte_EN = models.TextField( default = "")  # Texte de la question en anglais sur la page
    typeofquestion = ListCharField(
        base_field=models.CharField(max_length=10),
        size=5,
        max_length=(5 * 11),  # 5 * 10 character nominals, plus commas
        default = [],
    )
    partie = models.CharField(max_length=100)  # Exemple : "Mise en sécurité"
    noms_photos = models.CharField(max_length=255, blank=True, null=True)  # Exemple : "BMV.PNG"
    pictogrammes = models.CharField(max_length=255, blank=True, null=True)  # Exemple : "N/A"
    info_comp = models.TextField(blank=True, default="")

    # Questions suivantes
    id_question_suivante_1 = models.CharField(max_length=10, blank=True, null=True)
    partie_question_suivante_1 = models.CharField(max_length=100, blank=True, null=True)
    question_suivante_1_texte = models.TextField( default="", blank=True, null=True)

    id_question_suivante_2 = models.CharField(max_length=10, blank=True, null=True)
    partie_question_suivante_2 = models.CharField(max_length=100, blank=True, null=True)
    question_suivante_2_texte = models.TextField( default="", blank=True, null=True)

    id_question_suivante_3 = models.CharField(max_length=10, blank=True, null=True)
    partie_question_suivante_3 = models.CharField(max_length=100, blank=True, null=True)

    id_question_suivante_4 = models.CharField(max_length=10, blank=True, null=True)
    partie_question_suivante_4 = models.CharField(max_length=100, blank=True, null=True)

    id_question_suivante_5 = models.CharField(max_length=10, blank=True, null=True)
    partie_question_suivante_5 = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_question', 'partie'], name='unique_id_question_partie')
        ]

    def __str__(self):
        return f"Question {self.id_question}: {self.question_texte_FR[:50]}"

class Commentaire(models.Model):
    diagnostic_id = models.IntegerField()
    partie = models.CharField(max_length=100)  # Exemple : "Mise en sécurité"
    id_question = models.CharField(max_length=10)  # Peut être '1', '1.0', etc.
    commentaire = models.TextField()  # Contenu du commentaire
    datetime = models.DateTimeField(default=now)  # Date et heure de création

    def __str__(self):
        return f"Commentaire {self.id} - Diagnostic {self.diagnostic_id}"


class Cause(models.Model):
    Partie = models.CharField(max_length=100, default = "Mise en sécurité")
    Indice = models.CharField(max_length=10)

    # Causes racines et des résolutions en français
    cause_racine_1_FR = models.CharField(max_length=100, blank=True, null=True)
    cause_racine_2_FR = models.CharField(max_length=100, blank=True, null=True)
    resolution_1_FR = models.CharField(max_length=100, blank=True, null=True)
    resolution_2_FR = models.CharField(max_length=100, blank=True, null=True)

    # Causes racines et des résolutions en anglais
    cause_racine_1_EN = models.CharField(max_length=100, blank=True, null=True)
    cause_racine_2_EN = models.CharField(max_length=100, blank=True, null=True)
    resolution_1_EN = models.CharField(max_length=100, blank=True, null=True)
    resolution_2_EN = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Causes / Résolution n°{self.Indice}: partie {self.Partie}"
