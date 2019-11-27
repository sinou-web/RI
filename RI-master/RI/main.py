#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:59:54 2018

@author: izan
"""

""" ***** partie appels de fonction et test  ***** """
import os
DIR = "./TPRI"import FichierInverse, ModeleVect
FI = FichierInverse.FichierInverse()
fichierInverse = FI.reading_directory(DIR)
MV = ModeleVect.Vectoriel()
print(MV.VectoriserRequete2(fichierInverse,"jane austen volume"))

#FI = FichierInverse()
##fichier inverse -> frequences
#fichierInverse = FI.reading_directory(DIR)

#print(getDocsOfWordFreq("emma",fichierInverse),"\n \n")
#print(getWordsOfDocFreq("austen-emma.txt",fichierInverse),"\n \n"))
#print(fichierInverse['emma']['chesterton-ball.txt'])

##fichier inverse -> poids
#fichierPoids = tfidf(fichierInverse,len(os.listdir("./TPRI")))
#print(getDocsOfWordPoids("emma",fichierPoids),"\n \n"))
#print(getWordsOfDocPoids("austen-emma.txt",fichierPoids),"\n \n"))
#print(len(fichierPoids))

##requete 
#requeteB = requeteBoolean(fichierInverse)
#print(requeteB)
#requeteB = "(jane and austen) and not volume"
#print(requeteB)

#requeteV = requeteVectPoids(fichierInverse,0)
#print(requeteV)
#requeteV = {'jane': 1, 'austen': 1, 'volume':0}
#print(requeteV)

##modele boolean
#print("\n *************** modeleBoolean ************** \n Requete = ",requeteB,"\n doc pertinents = ",modeleBoolean(DIR,fichierInverse, requeteB))

##modele vectoriel
#print("\n *************** modeleVectoriel ************** \n Requete = ",requeteV,"\n\n doc pertinents = ",modeleVect(DIR,fichierInverse, requeteV))

