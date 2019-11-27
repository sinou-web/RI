#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:02:39 2018

@author: izan
"""

""" ******************************************************************** """
""" ************************* modele boolean *************************** """

class Boolean():
        
    """ creation d'une requete du modele boolean aléatoirement """
    def requeteBoolean(self,fichierInverse):
        from random import randint
        
        operators = ["and","or"," or not","and not"]
        requete = []
        
        if randint(0,1) == 1:
            requete.append("not")
            
        #pour un nombre i aléatoire de termes
        for i in range(randint(1,4)):
            requete.append(list(fichierInverse.keys())[randint(0,len(fichierInverse)-1)])
            requete.append(operators[randint(0,len(operators)-1)])
        
        requete.append(list(fichierInverse.keys())[randint(0,len(fichierInverse)-1)])
        return ' '.join(requete)
    
    
    
    def traitementWords(self,fichierInverse, requete, document):
        from nltk.tokenize import word_tokenize
        listeWords = word_tokenize(requete,language='english',preserve_line='true')
        NewListe = []
        
        for word in listeWords:
            if word not in ["and","or","not","(",")"]:
                if(fichierInverse[word].get(document, "none") == "none"):
                    NewListe.append("0")
                else:
                    NewListe.append("1")
            else:
                NewListe.append(word)
    
        return(NewListe)
        
    
    
    """ Modele Boolean : la liste des document pertinent pour une requete R """
    def modeleBoolean(self,DIR,fichierInverse, requete):
        import os
        listDocsPertinents = []
        
        for doc in os.listdir(DIR):
            liste = self.traitementWords(fichierInverse,requete, doc)
            chaine = ' '.join(liste)
            ok = (eval(chaine))
                        
            if ok == 1:#si tous les termes de la requete corresponde au "doc"
                listDocsPertinents.append(doc)
                
        return listDocsPertinents
    

