// Fonction pour ouvrir le popup accès logigramme
function openPopup_logig() {
    document.getElementById("popup-logig").style.visibility = "visible";
    document.getElementById("overlay").style.display = "block";
}
// Fonction pour fermer le popup accès logigramme
function closePopup_logig() {
    document.getElementById("popup-logig").style.visibility = "hidden";
    document.getElementById("overlay").style.display = "none";
}

// Fonction pour ouvrir le popup de commentaire
function openPopup_comm() {
    document.getElementById("popup-comm").style.visibility = "visible";
    document.getElementById("overlay").style.display = "block";
}
// Fonction pour fermer le popup de commentaire
function closePopup_comm() {
    document.getElementById("popup-comm").style.visibility = "hidden";
    document.getElementById("overlay").style.display = "none";
}

// Fonction pour ouvrir le popup illustration de la question
function openPopup_img() {
    document.getElementById("popup-img").style.visibility = "visible";
    document.getElementById("overlay").style.display = "block";
}
// Fonction pour fermer le popup illustration de la question
function closePopup_img() {
    document.getElementById("popup-img").style.visibility = "hidden";
    document.getElementById("overlay").style.display = "none";
}

// Fonction pour ouvrir le popup informations complémentaires
function openPopup_info() {
    document.getElementById("popup-info").style.visibility = "visible";
    document.getElementById("overlay").style.display = "block";
}
// Fonction pour fermer le popup informations complémentaires
function closePopup_info() {
    document.getElementById("popup-info").style.visibility = "hidden";
    document.getElementById("overlay").style.display = "none";
}

function envoyerCommentaire() {
    let commentaireForm = document.getElementById("commentaireForm");

    if (commentaireForm) {
        // Préparation des données du formulaire
        let formData = new FormData(commentaireForm);

        // Envoi des données avec Fetch API
        fetch(commentaireForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value // CSRF Token
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            let message = document.getElementById("message");

            if (data.success) {
                // Affichage du message de succès
                message.innerHTML = "<span style='color: white;'>Commentaire enregistré avec succès !</span>";
                
                // Réinitialisation du formulaire
                commentaireForm.reset();
                
                // Fermeture du popup après 1,5s
                setTimeout(closePopup_comm, 1500);
                
                // Affichage du message popup
                let confirmationPopup = document.getElementById("confirmationPopup");
                confirmationPopup.style.display = "block";  // Affiche le popup
                
                // Masquer le popup après 3 secondes
                setTimeout(() => {
                    confirmationPopup.style.display = "none"; // Cache le popup
                }, 3000); // Le popup sera caché après 3 secondes

                // Rafraîchissement de la page après 1,5 secondes
                setTimeout(() => {
                    window.location.reload();  // Rafraîchit la page actuelle
                }, 1500);
            } else {
                message.innerHTML = "<span style='color: red;'>Erreur lors de l'enregistrement.</span>";
            }
        })
        .catch(error => console.error("Erreur :", error));  // Gérer les erreurs de la requête fetch
    }
}


