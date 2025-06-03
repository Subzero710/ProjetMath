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

def exo1(simulateur):
    t = ['A','B','C','D','E']
    process = []
    tests = []
    for i in range(1000):
        count = 0
        for loop in range(1000):
            if (simulateur.administrer_traitement(t[randint(0,4)])):
                count+=1
        process.append(count)
    mean = np.mean(process)
    spread = np.std(process)

    response = f"Success of treatment for {mean/10}% of patients with a spread of {spread/10}%"
    return response

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
    print(exo1(simulator))


