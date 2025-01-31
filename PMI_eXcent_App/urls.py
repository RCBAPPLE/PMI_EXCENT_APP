from django.urls import path

from . import views

app_name = "PMI_eXcent_App"

urlpatterns = [

    path('', views.page_initial, name='page_initial'),

    # Routes pour l'accueil avec langue
    path('accueil/<str:lang>/', views.page_accueil, name='page_accueil'),

    # Routes de diagnostic
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>/<int:NBreponse>', views.page_question, name='page_question'),
    path('enregistrer_commentaire/', views.enregistrer_commentaire, name='enregistrer_commentaire'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>/precedente', views.page_precedente, name='page_precedente'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_solution>/<str:txt_solution>/results', views.page_results, name='results'),
    # Route pour enregistrer les commentaires
    path('enregistrer_commentaire/', views.enregistrer_commentaire, name='enregistrer_commentaire'),

    # Routes pour la navigation
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>', views.saut_partie_page_bilan, name='saut_partie_page_bilan'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>/<str:last_partie>/<str:last_id_question>', views.saut_partie_page_question, name='saut_partie_page_question'),

    # Routes pour l'export
    path('export/pdf/<str:lang>/<int:diagnostic_id>/', views.generate_pdf, name='export_pdf'),
    path('export/excel/<str:lang>/<int:diagnostic_id>/', views.generate_excel_based_on_language, name='export_excel_language'),
]