import pandas as pd
from .models import Template_Question, Cause


import os

# Affiche le répertoire de travail actuel
current_path = os.getcwd()
print(f"Le chemin actuel est : {current_path}")

# Liste des noms de feuilles (équivalent aux parties)
SHEET_NAMES = ["Mise en sécurité", "Observation et examen", "Alimentation", "Levage", "Ouverture", "Roulage"]

def load_excel_database(file_path):
    # Lire toutes les feuilles du fichier Excel
    sheets = pd.read_excel(file_path, sheet_name=None, engine='openpyxl', dtype=object )  # Retourne un dictionnaire {sheet_name: DataFrame}

    # Charger les données pour chaque feuille (chaque partie)
    for sheet_name, data in sheets.items():
        if sheet_name in SHEET_NAMES:
            print(f"Chargement de la partie : {sheet_name}")
            load_template_question(data)
        elif sheet_name == "Causes Racines et Résolutions":
            print("Chargement de causes et résolutions")
            load_causes(data)
        else:
            print(f"Feuille inconnue ignorée : {sheet_name}")



def load_template_question(data):
    """
    Charge les questions d'une feuille Excel spécifique dans la base de données.
    Le paramètre `partie` est dérivé du nom de la feuille Excel.
    """

    for index, row in data.iterrows():

        try:

            # Utilisation de la fonction convert_to_string pour convertir les valeurs
            id_question = str(row['Id Question']).strip()
            partie = str(row['Partie (ex: Mise en Sécurité, Observations et examen, Diagnostic ou Résolution)']).strip()

            # Assurez-vous que l'id_question et partie sont uniques pour chaque enregistrement
            # Utilisation de `update_or_create` pour éviter les doublons
            if partie == "Observations et examen" :
                Template_Question.objects.update_or_create(
                    id_question=id_question,
                    partie=partie,
                    defaults={
                        'question_texte_FR': str(row['Question de la page']).strip(),
                        'question_texte_EN': str(row['Question en anglais']).strip(),
                        'typeofquestion': str(row['Type de question']).split(",") if pd.notna(row['Type de question']) else [],  # On suppose que les types de question sont séparés par des virgules
                        'noms_photos': str(row['Noms photos (ex: img.png)']).strip() if pd.notna(row['Noms photos (ex: img.png)']) else None,
                        'pictogrammes': str(row['Pictogrammes']).strip() if pd.notna(row['Pictogrammes']) else None,
                        'info_comp': str(row['Informations complémentaires pour cette question']).strip(),

                        'id_question_suivante_1': str(row['Id Question suivante si Oui (si question sans Oui ou Non, mettre par défaut sous Oui)']).strip() if pd.notna(row['Id Question suivante si Oui (si question sans Oui ou Non, mettre par défaut sous Oui)']) else None,
                        'partie_question_suivante_1': str(row['Partie Question suivante si Oui']).strip() if pd.notna(row['Partie Question suivante si Oui']) else None,
                        'question_suivante_1_texte': str(row['Question suivante si Oui']).strip(),

                        'id_question_suivante_2': str(row['Id Question suivante si Non']).strip() if pd.notna(row['Id Question suivante si Non']) else None,
                        'partie_question_suivante_2': str(row['Partie Question suivante si Non']).strip() if pd.notna(row['Partie Question suivante si Non']) else None,
                        'question_suivante_2_texte': str(row['Questions suivante si Non']).strip(),

                        'id_question_suivante_3': str(row['Id Question si Réponse 3']).strip() if pd.notna(row['Id Question si Réponse 3']) else None,
                        'partie_question_suivante_3': str(row['Partie Question si Réponse 3']).strip() if pd.notna(row['Partie Question si Réponse 3']) else None,

                        'id_question_suivante_4': str(row['Id Question si Réponse 4']).strip() if pd.notna(row['Id Question si Réponse 4']) else None,
                        'partie_question_suivante_4': str(row['Partie Question suivante si Réponse 4']).strip() if pd.notna(row['Partie Question suivante si Réponse 4']) else None,

                        'id_question_suivante_5': str(row['Id Question si Réponse 5']).strip() if pd.notna(row['Id Question si Réponse 5']) else None,
                        'partie_question_suivante_5': str(row['Partie Question suivante si Réponse 5']).strip() if pd.notna(row['Partie Question suivante si Réponse 5']) else None,
                    }
                )
            else :
                Template_Question.objects.update_or_create(
                    id_question=id_question,
                    partie=partie,
                    defaults={
                        'question_texte_FR': str(row['Question de la page']).strip(),
                        'question_texte_EN': str(row['Question en anglais']).strip(),
                        'typeofquestion': str(row['Type de question']).split(",") if pd.notna(row['Type de question']) else [],  # On suppose que les types de question sont séparés par des virgules
                        'noms_photos': str(row['Noms photos (ex: img.png)']).strip() if pd.notna(row['Noms photos (ex: img.png)']) else None,
                        'pictogrammes': str(row['Pictogrammes']).strip() if pd.notna(row['Pictogrammes']) else None,
                        'info_comp': str(row['Informations complémentaires pour cette question']).strip(),
                        
                        'id_question_suivante_1': str(row['Id Question suivante si Oui (si question sans Oui ou Non, mettre par défaut sous Oui)']).strip() if pd.notna(row['Id Question suivante si Oui (si question sans Oui ou Non, mettre par défaut sous Oui)']) else None,
                        'partie_question_suivante_1': str(row['Partie Question suivante si Oui']).strip() if pd.notna(row['Partie Question suivante si Oui']) else None,
                        'question_suivante_1_texte': str(row['Question suivante si Oui']).strip(),

                        'id_question_suivante_2': str(row['Id Question suivante si Non']).strip() if pd.notna(row['Id Question suivante si Non']) else None,
                        'partie_question_suivante_2': str(row['Partie Question suivante si Non']).strip() if pd.notna(row['Partie Question suivante si Non']) else None,
                        'question_suivante_2_texte': str(row['Questions suivante si Non']).strip(),
                    }
                )

        except Exception as e:
            print(f"Erreur à la ligne {index + 2} dans la partie '{partie}': {e}. Question ignorée.")
    
    print(f"Partie '{partie}' chargée avec succès.")

def load_causes(data):
    """
    Charge les causes racines et résolutions d'une feuille Excel spécifique dans la base de données.
    """
    
    for index, row in data.iterrows():
        try:
            # Lecture des colonnes Excel avec une gestion des valeurs manquantes
            partie = str(row['Partie (ex: Mise en Sécurité, Observations et examen, Diagnostic ou Résolution)']).strip() if pd.notna(row['Partie (ex: Mise en Sécurité, Observations et examen, Diagnostic ou Résolution)']) else None
            indice = str(row['Indice de la mauvaise utilisation / Indice de la résolution']).strip() if pd.notna(row['Indice de la mauvaise utilisation / Indice de la résolution']) else None
            cause_racine_1_FR = str(row['Cause Racine 1 FR']).strip() if pd.notna(row['Cause Racine 1 FR']) else None
            cause_racine_2_FR = str(row['Cause Racine 2 FR']).strip() if pd.notna(row['Cause Racine 2 FR']) else None
            resolution_1_FR = str(row['Résolution 1 FR']).strip() if pd.notna(row['Résolution 1 FR']) else None
            resolution_2_FR = str(row['Résolution 2 FR']).strip() if pd.notna(row['Résolution 2 FR']) else None

            cause_racine_1_EN = str(row['Cause Racine 1 EN']).strip() if pd.notna(row['Cause Racine 1 EN']) else None
            cause_racine_2_EN = str(row['Cause Racine 2 EN']).strip() if pd.notna(row['Cause Racine 2 EN']) else None
            resolution_1_EN = str(row['Résolution 1 EN']).strip() if pd.notna(row['Résolution 1 EN']) else None
            resolution_2_EN = str(row['Résolution 2 EN']).strip() if pd.notna(row['Résolution 2 EN']) else None

            # Création d'un nouvel enregistrement dans la table Cause
            Cause.objects.update_or_create(
                Partie=partie,
                Indice=indice,
                cause_racine_1_FR=cause_racine_1_FR,
                cause_racine_2_FR=cause_racine_2_FR,
                resolution_1_FR=resolution_1_FR,
                resolution_2_FR=resolution_2_FR,
                cause_racine_1_EN=cause_racine_1_EN,
                cause_racine_2_EN=cause_racine_2_EN,
                resolution_1_EN=resolution_1_EN,
                resolution_2_EN=resolution_2_EN,
            )
        except Exception as e:
            
            print(f"Erreur à la ligne {index + 2} dans la partie '{partie}': {e}. Ligne ignorée.")
    
    print("Chargement des causes terminé avec succès.")




# Exemple d'utilisation
load_excel_database('PMI_eXcent_App/static/docs/Base_de_donnees_pages_de_questions.xlsx')
load_excel_database('PMI_eXcent_App/static/docs/BDD_causes_racines_et_resolutions.xlsx')
