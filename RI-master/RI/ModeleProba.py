#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:12:41 2018

@author: izan
"""
import nltk

class Proba():
    
    
    """ liste de mot -> requete """
    def VectoriserRequete2(self,fichierInverse,listMot):        
        fd = nltk.FreqDist(nltk.tokenize.word_tokenize(listMot))
        return fd
    
    
    #nombre de documents contenants le terme ti
    def DocsWithTi(self,N,fichierInverse,Fichiers,terme):
        nbr = 0
        for i in range(N):
            if Fichiers[i] in fichierInverse[terme].keys():
                nbr = nbr +1

        return nbr
    
    
    
    def ProbaAvecEch(self,N,Doc,fichierPoids, fichierInverse, Fichiers, listMot,R,ListDoc):
        from math import log10
        
        requete = self.VectoriserRequete2(fichierInverse,listMot)
        somme = 0
        for tq in requete.keys():
            Ri = self.getNbrDocPertinantTi_Ri(fichierInverse, Fichiers, tq,ListDoc)
            Ni = self.DocsWithTi(N,fichierInverse,Fichiers,tq)
            if Doc in fichierPoids[tq].keys():
                somme = somme + (fichierPoids[tq][Doc] * requete[tq] * log10(((Ri+0.5)/(R-Ri+0.5))/((Ni-Ri+0.5)/(N-Ni-R+Ri+0.5))))
            
        return somme
    
    
    def getNbrDocPertinantTi_Ri(self,fichierInverse, Fichiers, terme ,ListDoc):       
        Ri=0
        for i in ListDoc:
            if Fichiers[i] in fichierInverse[terme].keys() and fichierInverse[terme][Fichiers[i]] > 0:
                Ri = Ri + 1
        return Ri
    
    

    def ProbaSansEch(self,N,Doc,fichierPoids, fichierInverse, Fichiers, listMot):
        from math import log10
        
        requete = self.VectoriserRequete2(fichierInverse,listMot)
        somme = 0
        for tq in requete.keys():
            Ni = self.DocsWithTi(N,fichierInverse,Fichiers,tq)
            if Doc in fichierPoids[tq].keys():
                somme = somme + (fichierPoids[tq][Doc] * requete[tq] * log10((N-Ni+0.5)/(Ni+0.5)))
            
        return somme
    
    
    
    def ProbaBM25(self,N,Doc,fichierPoids, fichierInverse, Fichiers, listMot):
        from math import log10
        
        AVGdl = self.AVGlength(N,Fichiers)
        requete = self.VectoriserRequete2(fichierInverse,listMot)
        somme = 0
        k = 1.2
        b = 0.75
        for tq in requete.keys():
            Ni = self.DocsWithTi(N,fichierInverse,Fichiers,tq)
            if Doc in fichierPoids[tq].keys():
                Tfi = fichierInverse[tq][Doc]
                documents =open("./TPRI/"+Doc,"r").read()
                dl = len(documents)
                print(documents[1])
                somme = somme + ((((k+1)-Tfi)/(Tfi+k*(1-b)+(b*dl/AVGdl))) * log10((N-Ni+0.5)/(Ni+0.5)))
            
        return somme
    
    
    
    def AVGlength(self, N, Fichiers):
        AVG = 0
        for doc in Fichiers:
            documents =open("./TPRI/"+doc,"r").read()
            AVG = AVG + len(documents)
        return (AVG / N)
    
    
    
    