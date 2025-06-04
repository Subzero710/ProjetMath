# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:00:28 2025

@author: JDION
"""

import sys
import os
from random import randint
import numpy as np

dist_dir = os.path.join(os.path.dirname(__file__), "dist")
sys.path.insert(0, dist_dir)

import simulateur

SimulateurTraitement = simulateur.SimulateurTraitement

def exoObligatoireMono(simulateur):
    t = ['A','B','C','D','E']
    success_tracking = []   #nombre de succes totaux à l'instant T (1000 instants)
    total_success = 0
    it = 0
    nb_A , nb_B, nb_C, nb_D, nb_E= 0,0,0,0,0
    s_A, s_B, s_C, s_D, s_E = 0, 0, 0, 0, 0
    proportionality_tracking = []   #on track la distribution à chaque instant des tests effectués (1000 instants/iterations)
    for i in range(1000):
        traitement_choisi = t[randint(0,4)]
        if simulateur.administrer_traitement(traitement_choisi):
                total_success+=1
                if traitement_choisi == 'A':
                    nb_A += 1
                    s_A +=1
                elif traitement_choisi == 'B':
                    nb_B += 1
                    s_B +=1
                elif traitement_choisi == 'C':
                    nb_C += 1
                    s_C +=1
                elif traitement_choisi == 'D':
                    nb_D += 1
                    s_D +=1
                elif traitement_choisi == 'E':
                    nb_E += 1
                    s_E +=1
        else:
            if traitement_choisi == 'A':
                nb_A += 1
            elif traitement_choisi == 'B':
                nb_B += 1
            elif traitement_choisi == 'C':
                nb_C += 1
            elif traitement_choisi == 'D':
                nb_D += 1
            elif traitement_choisi == 'E':
                nb_E += 1
        it+=1
        success_tracking.append(total_success) #on suit l'evolution du nombre de succes
        it_prop = [nb_A/it, nb_B/it, nb_C/it, nb_D/it, nb_E/it] #la distribution des tests en % effectués jusque à cette iteration
        proportionality_tracking.append(it_prop)

    success_rates = [(s_A/nb_A),(s_B/nb_B),(s_C/nb_C),(s_D/nb_D),(s_E/nb_E)] #taux de reussite de chaque test

    return total_success,success_tracking,success_rates,proportionality_tracking

def exoObligatoireMoyenne(simulateur): #on applique un raisonnement "en Moyenne"
    all_total_success = []
    all_success_tracking = []
    all_success_rates = []
    all_proportions = []

    for loop in range(1000):
        total, success, rates, proportions = exoObligatoireMono(simulateur)
        all_total_success.append(total)
        all_success_tracking.append(success)
        all_success_rates.append(rates)
        all_proportions.append(proportions)

    mean_total_success = np.mean(all_total_success) #moyenne d'un tableau à 1 dimension
    mean_success_tracking= np.mean(all_success_tracking, axis=0) #moyenne des cellules d'un tableau à 2 dimension unes à unes
    mean_success_rates = np.mean(all_success_rates, axis=0)
    mean_proportions = np.mean(all_proportions, axis = 0)

    return mean_total_success,mean_success_tracking,mean_success_rates,mean_proportions

if __name__ == "__main__":
    simulator = SimulateurTraitement()
    '''
    while True:
        t = input("Choisissez un traitement (A, B, C, D, E) ou 'Q' pour quitter : ").strip().upper()
        if t == 'Q':
            break
        try:
            resultat = simulateur.administrer_traitement(t)
            print(f"Traitement {t}: {'Succès' if resultat else 'Échec'}")
        except ValueError as e:
            print(e)
    '''
    mean_total_success,mean_success_tracking,mean_success_rates,mean_proportions = exoObligatoireMoyenne(simulator)
    print("exoObligatoire OK")


