#!/usr/bin/env python
# coding: utf-8

# ### Initialisation

# In[ ]:


import json

import os
current_dir = os.path.dirname(__file__)

# In[ ]:


crit_list = []


# ### crit Dictionaries

# #### Attaque critique - Arme tranchante

# In[ ]:


# Unique Entries
critical_hits_bladed=dict([
    ("name", "critical_hits_bladed"),
    (1, "Incision profonde. Degats+1"),
    (3, "Incision vraiment profonde. Degats+2"),
    (5, "Plaies impressionantes. Degats+3, Armure PR-1"),
    (7, "Coup precis. Degats+4, Armure PR-2"),
    (9, "Coup precis de bourrin. Degats+5, Armure PR-3"),
    (11, "Partie armure detruite. PR=0"),
    (12, "Oeil creve. Degats+5 et modifs*"),
    (13, "Main tranche (1D6; droite=1-3; gauche=4-6). Degats+6 et modifs*"),
    (14, "Pied tranche (1D6; droite=1-3; gauche=4-6). Degats+6 et modifs*"),
    (15, "Bras tranche (1D6; droite=1-3; gauche=4-6). Degats+7 et modifs*"),
    (16, "Jambe tranche (1D6; droite=1-3; gauche=4-6). Degats+8 et modifs*"),
    (17, "Organe genitaux endommages (1D6; droite=1-3; gauche=4-6). Degats+5 et duree(1D6/min)"),
    (18, "Organe vitale endommages (1D6; droite=1-3; gauche=4-6). Degats+9  et duree(1D6/min)"),
    (19, "Blessure au coeur. Deces"),
    (20, "Blessure grave a la tête. Deces")
])
# Duplicate Entries
critical_hits_bladed.update(dict([
    (2, critical_hits_bladed[1]),
    (4, critical_hits_bladed[3]),
    (6, critical_hits_bladed[5]),
    (8, critical_hits_bladed[7]),
    (10, critical_hits_bladed[9])
]))
# Add To List
crit_list.append(critical_hits_bladed);


# #### Attaque critique - Armes contondantes

# In[ ]:


# Unique Entries
critical_hits_blunt=dict([
    ("name", "critical_hits_blunt"),
    (1, "Ematome impressionant. Degats+1"),
    (3, "Ematome et luxation d'un membre. Degats+2"),
    (5, "Fracture de cote. Degats+3"),
    (7, "Coup précis et dommages à l'armure. Degats+4, Armure PR-1"),
    (9, "Coup précis de bourrin et dommages à l'armure. Degats+5, Armure PR-2"),
    (11, "Une partie de l'armure est detruite. 1 piece armure PR=0"),
    (12, "Luxation du genou. Degats+3 et modifs*"),
    (13, "Main cassee (1D6; droite=1-3; gauche=4-6). Degats+3 et modifs*"),
    (14, "Pied ecrase (1D6; droite=1-3; gauche=4-6). Degats+3 et modifs*"),
    (15, "Bras casse (1D6; droite=1-3; gauche=4-6). Degats+4 et modifs*"),
    (16, "Jambe cassee (1D6; droite=1-3; gauche=4-6). Degats+5 et modifs*"),
    (17, "Organes genitaux ecrase. Degats+5 et modifs*"),
    (18, "Assomme. Inconscient"),
    (19, "Fracture ouverte du crane. Deces"),
    (20, "Ecrasement violent d'un organe vital. Deces")
])
# Duplicate Entries
critical_hits_blunt.update(dict([
    (2, critical_hits_blunt[1]),
    (4, critical_hits_blunt[3]),
    (6, critical_hits_blunt[5]),
    (8, critical_hits_blunt[7]),
    (10, critical_hits_blunt[9])
]))
# Add To List
crit_list.append(critical_hits_blunt);


# #### Attaque critique - Mains nues

# In[ ]:


# Unique Entries
critical_hits_hand2hand=dict([
    ("name", "critical_hits_hand2hand"),
    (1, "Ematome impressionant. Degats+1"),
    (3, "Ematome et luxation d'un membre. Degats+2"),
    (5, "Fracture du nez, hemorragie nasale. Degats+3"),
    (7, "Fracture de cote. Degats+4"),
    (9, "Coup precis de bourrin dans la tempe. degats+2; cible etourdie 3 assauts"),
    (11, "Coup precis au sternum. Cible etourdie 4 assauts"),
    (12, "Luxation de genou. Degats+3 et modifs*"),
    (13, "Main cassee (1D6; droite=1-3; gauche=4-6). Degats+3 et modifs*"),
    (14, "Machoire brisee. Degats+3; incapacite a parler"),
    (15, "Bras cassee (1D6; droite=1-3; gauche=4-6). Degats+4 et modifs*"),
    (16, "Organes genitaux ecrase, houlala. Degats+5 et modifs*"),
    (18, "Assomme. Inconscient"),
    (20, "Enfoncement du nez dans le cerveau; Deces")
])
# Duplicate Entries
critical_hits_hand2hand.update(dict([
    (2, critical_hits_hand2hand[1]),
    (4, critical_hits_hand2hand[3]),
    (6, critical_hits_hand2hand[5]),
    (8, critical_hits_hand2hand[7]),
    (10, critical_hits_hand2hand[9]),
    (17, critical_hits_hand2hand[16]),
    (19, critical_hits_hand2hand[18])
]))
# Add To List
crit_list.append(critical_hits_hand2hand);


# #### Attaque critique - Projectile

# In[ ]:


# Unique Entries
critical_hits_projectile=dict([
    ("name", "critical_hits_projectile"),
    (1, "Projectile bien place. Degats+1"),
    (3, "Projectile magistralement place. Degats+2"),
    (5, "Projectile dans une articulation du bras. Degats+3, AT/PRD-2"),
    (7, "Projectile dans une articulation de la jambe. Degats+3; mvt-50%"),
    (9, "Projectile dans un poumon. Degats+3, toutes caracs -1"),
    (12, "Projectile d maitre. Degats+5"),
    (17, "En plein dans les organes genitaux, bien fait! Degats+5 et duree**"),
    (18, "Organe vital endommage. Degats+6 et duree**"),
    (19, "Coeur transperce. Deces"),
    (20, "Oeil et cerveau transperce, bien fait! Deces")
])
# Duplicate Entries
critical_hits_projectile.update(dict([
    (2, critical_hits_projectile[1]),
    (4, critical_hits_projectile[3]),
    (6, critical_hits_projectile[5]),
    (8, critical_hits_projectile[7]),
    (10, critical_hits_projectile[9]),
    (11, critical_hits_projectile[9]),
    (13, critical_hits_projectile[12]),
    (14, critical_hits_projectile[12]),
    (15, critical_hits_projectile[12]),
    (16, critical_hits_projectile[12])
]))
# Add To List
crit_list.append(critical_hits_projectile);


# #### Parade critique

# In[ ]:


# Unique Entries
critical_hits_block=dict([
    ("name", "critical_hits_block"),
    (1, "Mais non en fait, la parade etait normale"),
    (3, "Ennemi repousse. Assaut rate"),
    (6, "Ennemi trebuche. Subit 1 attaque imparable"),
    (8, "Ennemi tombe. Subit 2 attaques imparables"),
    (10, "Ennemi lache son arme a 1D6 m. Il combat a main nues"),
    (13, "Ennemi casse son arme. Il combat a main nues"),
    (16, "Ennemi recoit un coup de votre arme. Il subit des degats"),
    (19, "Ennemi subit un coup critique avec votre arme. Degats de la table critique"),
    (20, "Ennemi, ce loser, subit un coup critique avec votre arme. Degats de la table critique")
])
# Duplicate Entries
critical_hits_block.update(dict([
    (2, critical_hits_block[1]),
    (4, critical_hits_block[3]),
    (5, critical_hits_block[3]),
    (7, critical_hits_block[6]),
    (9, critical_hits_block[8]),
    (11, critical_hits_block[10]),
    (12, critical_hits_block[10]),
    (14, critical_hits_block[13]),
    (15, critical_hits_block[13]),
    (17, critical_hits_block[16]),
    (18, critical_hits_block[16])
]))
# Add To List
crit_list.append(critical_hits_block);


# #### Maladresse - Standard

# In[ ]:


# Unique Entries
clumsy_hits_standard=dict([
    ("name", "clumsy_hits_standard"),
    (1, "Rattrape son erreur in extremis. Attaque rate uniquement"),
    (3, "Trebuche et chute maladroitement. Rate 2 assauts"),
    (6, "Frappe un allie proche vers la gauche. Degats sur allie"),
    (8, "Frappe un allie proche vers la droite. Degats sur allie"),
    (10, "Lache son arme comme un loser. Combats mains nues, change d'arme"),
    (13, "Casse son arme (selon point rupture). Combats mains nues, change d'arme"),
    (16, "Se blesse tout seul comme un cake. Tirer des degats sur le combattant"),
    (19, "Se blesse tres severement de facon atroce et douloureuse. Degats sur le combattant (critique)"),
    (20, "Perds un oeil (D1-2) un doigt (D3-6). Blessure grave**")
])
# Duplicate Entries
clumsy_hits_standard.update(dict([
    (2, clumsy_hits_standard[1]),
    (4, clumsy_hits_standard[3]),
    (5, clumsy_hits_standard[3]),
    (7, clumsy_hits_standard[6]),
    (9, clumsy_hits_standard[8]),
    (11, clumsy_hits_standard[10]),
    (12, clumsy_hits_standard[10]),
    (14, clumsy_hits_standard[13]),
    (15, clumsy_hits_standard[13]),
    (17, clumsy_hits_standard[16]),
    (18, clumsy_hits_standard[16])
]))
# Add To List
crit_list.append(clumsy_hits_standard);


# #### Maladresse - Sortileges

# In[ ]:


# Unique Entries
clumsy_hits_spells=dict([
    ("name", "clumsy_hits_spells"),
    (1, "Rattrapage de derniere minute, sacre veinard. Sort echoue seulement"),
    (3, "Sort s'evapore. 50% PA investi perdu"),
    (4, "Sort s'evapore. 100% PA investi perdu"),
    (5, "Le sort frappe la personne le plus proche sur la droite. Selon effet du sort"),
    (7, "Le sort frappe la personne le plus proche sur la gauche. Selon effet du sort"),
    (9, "Le sort frappe la personne le plus proche sur l'arriere. Selon effet du sort"),
    (11, "Le sort frappe la personne le plus proche sur l'avant. Selon effet du sort"),
    (13, "Choc en retour. Sort reviens sur lanceur selon effet du sort"),
    (17, "Sort fou, zone d'effet multiplie par 1D10 m. Selon effet du sort"),
    (19, "Sort entropique (sors de nulle part frappe n'importe qui, MJ decide) a destination d'un ennemi. Voir sort entropique"),
    (20, "Sort entropique (sors de nulle part frappe n'importe qui, MJ decide) a destination d'un allie. Voir sort entropique")
])
# Duplicate Entries
clumsy_hits_spells.update(dict([
    (2, clumsy_hits_spells[1]),
    (6, clumsy_hits_spells[5]),
    (8, clumsy_hits_spells[7]),
    (10, clumsy_hits_spells[9]),
    (12, clumsy_hits_spells[11]),
    (14, clumsy_hits_spells[13]),
    (15, clumsy_hits_spells[13]),
    (16, clumsy_hits_spells[13]),
    (18, clumsy_hits_spells[17])
]))
# Add To List
crit_list.append(clumsy_hits_spells);


# #### Maladresse - Arme a jets

# In[ ]:


# Unique Entries
clumsy_hits_projectile=dict([
    ("name", "clumsy_hits_projectile"),
    (1, "Rattrape son erreur in extremis. Projectile n'atteint pas sa cible"),
    (3, "Lache son arme comme un loser. combat main nues ou change d'armes"),
    (6, "Frappe un allie proche sur la gauche. Degats a calculer"),
    (8, "Frappe un allie proche sur la droite. Degats a calculer"),
    (10, "Frappe allie le plus lointain. Degats a calculer"),
    (13, "Casse son arme (selon point rupture). Combats a main nues"),
    (16, "Se tire dans le pied. Degats de l'arme+2"),
    (19, "Se blesse tres severement dans un grand cri haineux. Degats sur le combattant (critique)"),
    (20, "Creve l'oeil de l'allie le plus proche. Blessure grave**")
])
# Duplicate Entries
clumsy_hits_projectile.update(dict([
    (2, clumsy_hits_projectile[1]),
    (4, clumsy_hits_projectile[3]),
    (5, clumsy_hits_projectile[3]),
    (7, clumsy_hits_projectile[6]),
    (9, clumsy_hits_projectile[8]),
    (11, clumsy_hits_projectile[10]),
    (12, clumsy_hits_projectile[10]),
    (14, clumsy_hits_projectile[13]),
    (15, clumsy_hits_projectile[13]),
    (17, clumsy_hits_projectile[16]),
    (18, clumsy_hits_projectile[16])
]))
# Add To List
crit_list.append(clumsy_hits_projectile);


# #### Maladresse - Main nues

# In[ ]:


# Unique Entries
clumsy_hits_hand2hand=dict([
    ("name", "clumsy_hits_hand2hand"),
    (1, "Rattrape son erreur in extremis. Attaque echoue seulement"),
    (3, "Tombe et s'ecrase le nez par terre.Perd 2 assauts, 2BL"),
    (11, "Frappe un allie proche vers la gauche. Degats sur allie"),
    (13, "Frappe un allie proche vers la droite. Degats sur allie"),
    (15, "Se brise la main tout seul comme une tanche. 3BL, blessure grave**"),
    (17, "Se casse un bras betement. 6BL, blessure grave**"),
    (20, "Tombe en arriere et s'assomme. Perte de connaissance")
])
# Duplicate Entries
clumsy_hits_hand2hand.update(dict([
    (2, clumsy_hits_hand2hand[1]),
    (4, clumsy_hits_hand2hand[3]),
    (5, clumsy_hits_hand2hand[3]),
    (6, clumsy_hits_hand2hand[3]),
    (7, clumsy_hits_hand2hand[3]),
    (8, clumsy_hits_hand2hand[3]),
    (9, clumsy_hits_hand2hand[3]),
    (10, clumsy_hits_hand2hand[3]),
    (12, clumsy_hits_hand2hand[11]),
    (14, clumsy_hits_hand2hand[13]),
    (16, clumsy_hits_hand2hand[15]),
    (18, clumsy_hits_hand2hand[17]),
    (19, clumsy_hits_hand2hand[17])
]))
# Add To List
crit_list.append(clumsy_hits_hand2hand);


# ### Generate json from crit dictionaries

# In[ ]:

for crit_table in crit_list:
    json_object = json.dumps(crit_table, indent=4)
    file_path = os.path.join(current_dir, crit_table["name"] + ".json")
    with open(file_path, "w") as output_file:
        output_file.write(json_object)


# In[ ]:




