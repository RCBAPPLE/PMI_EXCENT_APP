from django.contrib import admin

from .models import *

"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
"""

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

class CausesAdmin(admin.ModelAdmin):
    list_display = ["Indice","Partie"]
    list_filter = ["Partie"]


admin.site.register(Diagnostic, DiagnosticAdmin)
admin.site.register(Template_Question, QuestionAdmin)
admin.site.register(Causes, CausesAdmin)