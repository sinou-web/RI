#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:01:42 2018

@author: izan
"""

""" ******************************************************************** """
""" ************************* modele vectoriel ************************* """
import nltk

class Vectoriel():
    
    """ creation d'une requete pondérée du modele Vect  aléatoirement """
    def requeteVectPoids(self,fichierInverse,typePoids):#typePoids=0 simple; typePoids=1 pondéré 
        from random import randint
        from nltk import defaultdict
        
        requete = defaultdict(int)
        #pour un certain nombre de termes du fichier inverse
        for i in range(randint(1,4)):
            #choisir un terme au hasard
            terme = list(fichierInverse.keys())[randint(0,len(fichierInverse)-1)]
            
            #mettre dans la requete les termes avec poids entre 1 et 10
            if(typePoids == 0):
                requete[terme]=1
            else:
                requete[terme]=randint(1,10)
      
        return requete
    
    """ liste de mot -> requete """
    def VectoriserRequete2(self,fichierInverse,listMot):
        vecRequete = []
        
        fd = nltk.FreqDist(nltk.tokenize.word_tokenize(listMot))
        for terme in fichierInverse:
            if terme in fd.keys():
                vecRequete.append(fd.get(terme))
            else:
                vecRequete.append(0)
            
        return vecRequete
    
    
    """ vectoriser la requete """
    def VectoriserRequete(self,fichierInverse, requete):
        vecRequete = []
    
        for terme in fichierInverse:
            if terme in requete.keys():
                vecRequete.append(requete[terme])
            else:
                vecRequete.append(0)
            
        return vecRequete
            
    
    """ vectoriser un document """
    def VectoriserDoc(self,fichierInverse, document):
        vecDoc = []
        for terme in fichierInverse:
            vecDoc.append(fichierInverse[terme].get(document, 0) )
        return vecDoc
    
    
    """ retourn la similitude entre la requete et le doc donné """
    def ProduitInterne(self,fichierInverse, document, requete):
        sim = 0
        for i in range(len(document)):
            sim = sim + (requete[i] * document[i] )
        return sim
    
    
    
    """ retourn la similitude entre la requete et le doc donné """
    def CoefDeDice(self,fichierInverse, document, requete):
        somme1 = 0
        somme2 = 0
        somme3 = 0
        for i in range(len(document)):
            somme1 = somme1 + (requete[i] * document[i] )
            somme2 = somme2 + (requete[i]**2)
            somme3 = somme3 + (document[i]**2)
        
        if(somme2 == somme3 ==0):
            sim=0
        else:
            sim = 2*somme1 / (somme2 + somme3)
        return sim
        
    
    """ retourn la similitude entre la requete et le doc donné """
    def Cosinus(self,fichierInverse, document, requete):
        somme1 = 0
        somme2 = 0
        somme3 = 0
        for i in range(len(document)):
            somme1 = somme1 + (requete[i] * document[i] )
            somme2 = somme2 + (requete[i]**2)
            somme3 = somme3 + (document[i]**2)
        
        if(somme2 ==0 or somme3 ==0):
            sim=0
        else:
            sim = somme1 / (somme2 * somme3)**(1/2)
        return sim
        
    
    """ retourn la similitude entre la requete et le doc donné """
    def Jaccard(self,fichierInverse, document, requete):
        somme1 = 0
        somme2 = 0
        somme3 = 0
        for i in range(len(document)):
            somme1 = somme1 + (requete[i] * document[i] )
            somme2 = somme2 + (requete[i]**2)
            somme3 = somme3 + (document[i]**2)
        
        var = somme2 + somme3 - somme1
        
        if(var == 0):
            sim=0
        else:
            sim = somme1 / var
        return sim
        
    
    
        
    """ applique une fonction de similitude sur tous les docs et les retourn dans l'ordre de partinence """
    def modeleVect(self,DIR,fichierInverse, req,formule):
        from nltk import defaultdict
        import operator,os
        
        requete = self.VectoriserRequete2(fichierInverse,req)
        
        #dictionnaire de la forme ("doc":valeurSim)
        listDocsPertinents = defaultdict(int)
        
        #pour chaque doc calculer la sim
        for doc in os.listdir(DIR):
            
            document = self.VectoriserDoc(fichierInverse,doc)
            
            if formule == "Produit Interne":
                sim = self.ProduitInterne(fichierInverse,document,requete)
            if formule == "Coeficient de Dice":
                sim = self.CoefDeDice(fichierInverse, document, requete)
            if formule == "Cosinus":
                sim = self.Cosinus(fichierInverse,document,requete)
            if formule == "Jaccard":
                sim = self.Jaccard(fichierInverse, document, requete)
            
            if(sim != 0):#liste des docs pertinents
                listDocsPertinents[doc]=sim
    
        #trier les docs pertinent dans l'ordre décroissant de similitude
        sortedListDoc = sorted(listDocsPertinents.items(), key=operator.itemgetter(1),reverse=True)
        return sortedListDoc
   

