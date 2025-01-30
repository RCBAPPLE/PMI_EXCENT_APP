from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import DiagnosticForm
from xhtml2pdf import pisa
from django.template.loader import get_template
import openpyxl
import os
import datetime
from django.conf import settings

from .models import *

def page_initial(request):

    lang = 'FR'  # Default language is French

    # Affichage initial
    form = DiagnosticForm(lang=lang)

    # Rendu de la page d'accueil avec le formulaire
    return HttpResponseRedirect(reverse("PMI_eXcent_App:page_accueil", kwargs={"lang": lang}))

def page_accueil(request, lang):
    if lang not in ['FR', 'EN']:
        lang = 'FR'  # Default language is French

    if request.method == 'POST':
        # Gestion de la soumission du formulaire
        form = DiagnosticForm(request.POST, lang=lang)
        if form.is_valid():
            diagnostic = form.save()  # Sauvegarde de l'objet Diagnostic
            # Redirige vers une page des questions ou affiche un succès
            return render(request, 'PMI_eXcent_App/template_question.html', {
                'Diagnostic_id': diagnostic.id,
                'langue': lang,
                'question': get_object_or_404(Template_Question, partie="Mise en Sécurité", id_question="1"),})

        else:
            # Réafficher la page d'accueil avec les erreurs
            return render(request, 'PMI_eXcent_App/page_accueil.html', {
                'form': form,
                'langue': lang,
            })
    else:
        # Affichage initial
        form = DiagnosticForm(lang=lang)

    # Rendu de la page d'accueil avec le formulaire
    return render(request, 'PMI_eXcent_App/page_accueil.html', {
        'form': form,
        'langue': lang,
    })


def saut_partie(request, lang, diagnostic_id, partie, id_question):
    return render(request, 'PMI_eXcent_App/template_question.html', {
                'Diagnostic_id': diagnostic_id,
                'langue': lang,
                'question': get_object_or_404(Template_Question, partie=partie, id_question=id_question),})


def page_question (request, lang, diagnostic_id, partie, id_question, NBreponse):
    if lang not in ['FR', 'EN']:
        lang = 'FR'  # Default language is French


    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
    previous_question_data = Template_Question.objects.filter(partie=partie, id_question=id_question).values()[0]
    previous_question = get_object_or_404(Template_Question, pk=previous_question_data["id"])
    
    Result.objects.update_or_create(Diagnostic=diagnostic, Partie=partie, Question=previous_question.question_texte_FR, Réponse=previous_question.typeofquestion[NBreponse - 1])

    if NBreponse == 1:
        if previous_question.partie_question_suivante_1 == "Page de diagnostic":
            return HttpResponseRedirect(reverse("PMI_eXcent_App:results", args=(lang,diagnostic.id,partie,
                                            previous_question.id_question_suivante_1,previous_question.question_suivante_1_texte)))
        else :
            # Remplacer "Oui" par la logique de la réponse 1
            next_question_data = Template_Question.objects.filter(
                partie=previous_question.partie_question_suivante_1,
                id_question=previous_question.id_question_suivante_1
            ).values()[0]
    elif NBreponse == 2:
        if previous_question.partie_question_suivante_2 == "Page de diagnostic":
            return HttpResponseRedirect(reverse("PMI_eXcent_App:results", args=(lang,diagnostic.id,partie,
                                            previous_question.id_question_suivante_2,previous_question.question_suivante_2_texte)))
        else :
            next_question_data = Template_Question.objects.filter(
                partie=previous_question.partie_question_suivante_2,
                id_question=previous_question.id_question_suivante_2
            ).values()[0]
    elif NBreponse == 3:
        if previous_question.partie_question_suivante_3 == "Page de diagnostic":
            return HttpResponseRedirect(reverse("PMI_eXcent_App:results", args=(lang,diagnostic.id,partie,
                                            previous_question.id_question_suivante_3,previous_question.question_suivante_3_texte)))
        else :
            next_question_data = Template_Question.objects.filter(
            partie=previous_question.partie_question_suivante_3,
            id_question=previous_question.id_question_suivante_3
            ).values()[0]
    elif NBreponse == 4:
        if previous_question.partie_question_suivante_4 == "Page de diagnostic":
            return HttpResponseRedirect(reverse("PMI_eXcent_App:results", args=(lang,diagnostic.id,partie,
                                            previous_question.id_question_suivante_4,previous_question.question_suivante_4_texte)))
        else :
            next_question_data = Template_Question.objects.filter(
            partie=previous_question.partie_question_suivante_4,
            id_question=previous_question.id_question_suivante_4
            ).values()[0]
    elif NBreponse == 5:
        if previous_question.partie_question_suivante_5 == "Page de diagnostic":
            return HttpResponseRedirect(reverse("PMI_eXcent_App:results", args=(lang,diagnostic.id,partie,
                                            previous_question.id_question_suivante_5,previous_question.question_suivante_5_texte)))
        else :
            next_question_data = Template_Question.objects.filter(
            partie=previous_question.partie_question_suivante_5,
            id_question=previous_question.id_question_suivante_5
            ).values()[0]

    next_question = get_object_or_404(Template_Question, pk=next_question_data["id"])
    return render(request, 'PMI_eXcent_App/template_question.html', {
            'Diagnostic_id': diagnostic.id,
            'langue': lang,
            'question': next_question,
            'question_precedente': previous_question,

        })


def page_precedente(request, lang, diagnostic_id, partie, id_question):
    if lang not in ['FR', 'EN']:
        lang = 'FR'  # Default language is French

    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)

    # Récupérer la question actuelle
    current_question_data = Template_Question.objects.filter(partie=partie, id_question=id_question).values()[0]
    current_question = get_object_or_404(Template_Question, pk=current_question_data["id"])

    # Récupérer les résultats enregistrés pour identifier la dernière question répondue
    last_result = Result.objects.filter(Diagnostic=diagnostic).order_by('-id').first()
    last_result.delete()

    if last_result:
        # Retrouver la question précédente via le texte de la dernière réponse
        previous_question_data = Template_Question.objects.filter( 
                                              partie=last_result.Partie, 
                                              question_texte_FR=last_result.Question).values()[0]
        previous_question = get_object_or_404(Template_Question, pk=previous_question_data["id"])


        return render(request, 'PMI_eXcent_App/template_question.html', {
            'Diagnostic_id': diagnostic.id,
            'langue': lang,
            'question': previous_question,
            'question_precedente': current_question,
        })
    else:
        # Si aucune question précédente n'est trouvée, retourner à la page initiale
        return render(request, 'PMI_eXcent_App/template_question.html', {
            'Diagnostic_id': diagnostic.id,
            'langue': lang,
            'question': current_question,
        })



def page_results(request, lang, diagnostic_id, partie, id_solution, txt_solution):
    # Récupérer le diagnostic
    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
    
    # Récupérer les résultats associés
    results = Result.objects.filter(Diagnostic=diagnostic)
    
    # Initialiser la solution à None par défaut
    solution = None
    
    # Essayer de récupérer les données des solutions
    try:
        solution_data = Cause.objects.filter(
            Partie=partie,
            Indice=id_solution
        ).values()[0]  # Récupérer la première solution trouvée (si existante)
        
        # Si des données sont trouvées, récupérer l'objet Cause correspondant
        solution = Cause.objects.get(pk=solution_data["id"])
    except (IndexError, Cause.DoesNotExist):
        # Aucune solution trouvée ou erreur d'accès aux données
        pass

    # Rendre le template avec ou sans solution
    return render(request, 'PMI_eXcent_App/bilan_causes.html', {
        'Diagnostic': diagnostic,
        'results': results,
        'langue': lang,
        'Solution': solution,  # Peut être None si aucune solution n'est trouvée
        'Txt_autre': txt_solution, # Au cas où solution pas dans Bdd, affichage de secours
    })

def generate_pdf(request, diagnostic_id, lang):
    # Fetch the diagnostic data
    diagnostic = get_object_or_404(Diagnostic, pk=diagnostic_id)
    results = Result.objects.filter(Diagnostic=diagnostic)

    # Create context for the template
    context = {
        'diagnostic': diagnostic,
        'results': results,
        'langue': lang
    }

    # Load the template and render to a string
    template = get_template('PMI_eXcent_App/pdf_template.html')
    html = template.render(context)

    # Create the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Diagnostic_{diagnostic.Client}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return PDF file or an error message
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response


def generate_excel_based_on_language(request, diagnostic_id, lang):
    # Récupérer le diagnostic
    diagnostic = Diagnostic.objects.get(id=diagnostic_id)

    # Déterminer le template en fonction de la langue
    if lang == 'FR':
        template_path = os.path.join(settings.BASE_DIR, "PMI_eXcent_App/static/docs/template_RIN_fr.xlsx")
    else:
        template_path = os.path.join(settings.BASE_DIR, "PMI_eXcent_App/static/docs/template_RIN_en.xlsx")

    # Charger le template Excel
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active  # Feuille active

    # Remplir les cellules avec les données spécifiques
    ws["S6"] = diagnostic.Client  # Cellule S6 : Nom du client
    ws["S4"] = f"Date: {datetime.datetime.now().strftime('%d/%m/%Y')}"  # Cellule S4 : Date du jour
    ws["R15"] = "JacXson U70"  # Cellule R15 : Texte fixe
    ws["G17"] = diagnostic.SN_JacXson  # Cellule G17 : SN JacXson
    ws["N10"] = datetime.datetime.now().strftime('%d/%m/%Y')

    # Préparer la réponse HTTP avec le fichier Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="RIN_{diagnostic.Client}.xlsx"'
    wb.save(response)  # Sauvegarde le fichier dans la réponse
    return response