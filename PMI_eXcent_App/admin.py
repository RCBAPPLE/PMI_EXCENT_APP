from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):

    list_display = ["id_question", "question_texte_FR", "partie"]
    list_filter = ["partie"]
    search_fields = ["question_texte_FR"]



class ResultInline(admin.TabularInline):
    model = Result



class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ["pk","Client", "SN_JacXson", "Trigramme_Technicien"]
    fields = ["Client", "SN_JacXson", "Trigramme_Technicien"]
    inlines = [ResultInline]

class CauseAdmin(admin.ModelAdmin):
    list_display = ["Indice","Partie"]
    list_filter = ["Partie"]


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ["diagnostic_id","partie","id_question", "datetime"]
    list_filter = ["partie"]

admin.site.register(Diagnostic, DiagnosticAdmin)
admin.site.register(Template_Question, QuestionAdmin)
admin.site.register(Cause, CauseAdmin)
admin.site.register(Commentaire, CommentaireAdmin)