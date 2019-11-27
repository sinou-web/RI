import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk import defaultdict
class FichierInverse():
        
    def create_n_docuement(self,directory,n):
        list =nltk.corpus.gutenberg.fileids()
        print("\n".join(list))
        for element in list:
            f=open(directory+"/"+element,"w")
            f.write(" ".join(nltk.corpus.gutenberg.words(str(element))[:60]))
            f.close()
    
    """ creation du fichier inverse à partir des fichier du rep """
    def reading_directory(self,text):
     
    
        dic_inverse_string= defaultdict(defaultdict)
    
        # lecture de tous les document du repetroire donné
        for f in os.listdir(text):
            documents =open(text+"/"+f,"r").read()
            #normalisation du text
            documents=documents.lower()
    
            #tokenisation
            words=word_tokenize(documents,language='english',preserve_line='true')
            stopWords=set(stopwords.words('english'))
    
            #suppression des stopwords
            for w in words:
                   if w not in stopWords:
                       s = re.match("[éçùàa-zA-z]+", w)
                       if  s:
                          if f not in dic_inverse_string[w].keys():
                              #créer une entré du fichier courant pour le terme "w" init à 0
                              dic_inverse_string[w][f]=0
                          #incrémenter la fréquence du terme "w" dans le fichier "f"
                          dic_inverse_string[w][f] += 1
    
    #        #ecriture du fichier inverse dans un fichier text
    #        fm=open("resultat_inverse.txt","w")
    #        for i in dic_inverse_string:
    #            fm.write(i+":"+str(dic_inverse_string[i].items())+"\n")
    #        fm.close()
            
        return dic_inverse_string
    
    """ retourner la liste de (terme:frequence) d'un fichier donné """
    def getWordsOfDocFreq(self,document,fichierinverse):
    
        import nltk
        liste_doc=nltk.defaultdict(int)
    
        for terme in fichierinverse.keys():
            if document  in fichierinverse[terme]:
                liste_doc[terme]=fichierinverse[terme][document]
    #            print("mot:",terme,"freq:",liste_doc [terme])
    
    #    print(liste_doc)
        return liste_doc
        
    
    """ retourner la liste des document ou apparet un terme (doc:freq) donné """
    def getDocsOfWordFreq(self,word,fichierinverse):
        from nltk import defaultdict
    
        dic_document_frequency = defaultdict(int)
        for terme in fichierinverse.keys():
            if str(terme) == word:
                for l in fichierinverse[terme]:
                    dic_document_frequency[l]=fichierinverse[terme][l]
                    
    #    print(dic_document_frequency)
        return dic_document_frequency
    
    
    """ création du fichier inverse des poids """
    def tfidf(self,dictionnaire,nbdoc):
        from nltk import defaultdict
        import math
    
        poids_fichier = defaultdict(defaultdict)
    
        for terme in dictionnaire:
            #nbr de Docs ou apparait le terme
            Ni=len(self.getDocsOfWordFreq(terme,dictionnaire))
    
            for document in dictionnaire[terme]:
               # frequence maximal d'un terme dans le document
                Max = max(self.getWordsOfDocFreq(document,dictionnaire).values())
                poids=((dictionnaire[terme][document])/Max)*math.log((nbdoc/Ni)+1)
                
                if document not in poids_fichier[terme].keys():
                    poids_fichier[terme][document]=0
    
                poids_fichier[terme][document] = (poids)
                
    #    #affichage
    #    for ti in poids_fichier.keys():
    #        for d in poids_fichier[ti].keys():
    #         print(ti,":",d,":",poids_fichier[ti][d])
    
        return poids_fichier
        
    
    
    
    """ retourner la liste des document ou apparet un terme (doc:freq) donné """
    def getWordsOfDocPoids(self,document,dictionnaire_poids):
        return self.getWordsOfDocFreq(document,dictionnaire_poids)
    
    
    """ retourner la liste de (terme:poids) d'un fichier donné """
    def getDocsOfWordPoids(self,word,dictionnaire_poids):
        return self.getDocsOfWordFreq(word,dictionnaire_poids)
    
        


""" ********************************************** """




