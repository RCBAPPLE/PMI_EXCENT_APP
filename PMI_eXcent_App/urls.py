from django.urls import path

from . import views

app_name = "PMI_eXcent_App"

urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
    path('accueil/<str:lang>/', views.page_accueil, name='page_accueil'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>/<int:NBreponse>', views.page_question, name='page_question'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>', views.saut_partie, name='saut_partie'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_question>', views.page_precedente, name='page_precedente'),
    path('diagnostic/<str:lang>/<str:diagnostic_id>/<str:partie>/<str:id_solution>/<str:txt_solution>/results', views.page_results, name='results'),
    path('export/pdf/<str:lang>/<int:diagnostic_id>/', views.generate_pdf, name='export_pdf'),
    path('export/excel/<str:lang>/<int:diagnostic_id>/', views.generate_excel_based_on_language, name='export_excel_language'),
]