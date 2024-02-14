import streamlit as st
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Définir les dates de début et de fin
date_debut = datetime(2019, 10, 31)
date_fin = datetime(2024, 7, 31)
maintenant = datetime.now()

# Assurer que maintenant est entre date_debut et date_fin
if maintenant < date_debut:
    maintenant = date_debut
elif maintenant > date_fin:
    maintenant = date_fin

# Calculer le total des secondes et les secondes écoulées
total_secondes = (date_fin - date_debut).total_seconds()
secondes_ecoulees = (maintenant - date_debut).total_seconds()
secondes_restantes = (date_fin - maintenant).total_seconds()

# Calculer le pourcentage d'avancement
pourcentage_avancement = (secondes_ecoulees / total_secondes) * 100

# Calculer le temps restant
temps_restant = date_fin - maintenant
jours_restants = temps_restant.days
heures_restantes = temps_restant.seconds // 3600
minutes_restantes = (temps_restant.seconds % 3600) // 60

# Afficher la barre de progression et le pourcentage
# st.write(f"Avancement: {pourcentage_avancement:.2f}% avant le 31 aout 2024")
# st.progress(int(pourcentage_avancement))

# Calculer les mois restants de manière simplifiée
# Cette méthode donne une approximation et pourrait être affinée
# pour une précision accrue.
mois_restants, jours_restants = divmod(jours_restants, 30)

# Afficher le temps restant sans chiffres après la virgule
# st.write(f"Il reste {mois_restants} mois, {jours_restants} jours, {heures_restantes} heures, {minutes_restantes} minutes.")

st.header(f"DEPUIS LE 31 OCTOBRE 2019 ET AVANT LE 31 JUILLET 2024")

# Calculer le nombre total de jours entre les dates de début et de fin
total_jours = (date_fin - date_debut).days + 1  # +1 pour inclure la journée de fin

# Calculer le nombre de jours écoulés jusqu'à maintenant
jours_ecoules = (maintenant - date_debut).days + 1  # +1 pour inclure aujourd'hui si maintenant < date_fin

st.write(f"Il s'est écoulé {jours_ecoules} jours ensemble à distance.")
st.write(f"Il n'en reste plus que {total_jours - jours_ecoules} pour ne plus jamais se quitter.")

# Préparer la matrice des jours pour la visualisation
jours_matrice = np.array([1 if i < jours_ecoules else 0 for i in range(total_jours)])

# Déterminer le nombre de carrés par côté pour une grille carrée approximative
cote = int(np.ceil(np.sqrt(total_jours)))

# Redimensionner jours_matrice pour qu'elle s'adapte dans une grille carrée
jours_matrice.resize(cote*cote, refcheck=False)  # Remplit les valeurs manquantes avec des zéros (jours futurs non existants)

# Créer une figure pour la visualisation
plt.figure(figsize=(10, 10))
cmap = ListedColormap(['blue', 'green'])  # Bleu pour les jours à venir, vert pour les jours passés
plt.imshow(jours_matrice.reshape(cote, cote), cmap=cmap)
plt.axis('off')  # Masquer les axes pour ne voir que la grille

# Créer une figure pour la visualisation
plt.figure(figsize=(12, 12))  # Ajustez la taille au besoin
cmap = ListedColormap(['#0000FF', '#008000'])  # Utiliser des codes hexadécimaux pour bleu (jours à venir) et vert (jours passés)

# Ajuster l'affichage pour que chaque carré soit bien séparé
plt.imshow(jours_matrice.reshape(cote, cote), cmap=cmap, aspect='equal')

# Ajouter le quadrillage
# La fonction grid ne permet pas directement de s'aligner sur les bords des cellules de imshow,
# donc nous utilisons une approche alternative pour dessiner le quadrillage.
for x in range(cote + 1):
    plt.axhline(x - 0.5, lw=2, color='k', zorder=5)  # Horizontal lines
    plt.axvline(x - 0.5, lw=2, color='k', zorder=5)  # Vertical lines

plt.axis('off')  # Masquer les axes pour ne voir que la grille et le quadrillage

# Afficher la visualisation dans Streamlit
st.pyplot(plt)