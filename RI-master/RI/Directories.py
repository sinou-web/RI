import nltk
def create_n_docuement(directory,n):
    list =nltk.corpus.gutenberg.fileids()
    print("\n".join(list))
    for element in list:
        f=open(directory+"/"+element,"w")
        f.write(" ".join(nltk.corpus.gutenberg.words(str(element))[:60]))
        f.close()




def directory_creator(localpath,name):
    import os
    dirName = localpath+"/"+name

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


def frequency_fichier(fichier,motvides):
    import re
    f=open(fichier,"r").read()
    

    motvides="\\b|\\b".join(motvides)
    motvides ="(\\b"+motvides+"\\b)"
    print("join",motvides)

    f=re.sub(motvides,'',f)
    print("liste frequence after stopwords:",f)



    from collections import Counter

    f=f.split()
    resultat = Counter(f).most_common()
    #resultat.sort()
    print("sorted list of frequency:", resultat)

def stopwords(text):

    file = open("/home/masterubunto/Desktop/RI_tp/vide","r").readlines()
    l=[]
    for f in file :
        import re

        s= re.match("[éçùàa-zA-z']+",f)
        if  s :
            print("line:",s.string)
            l=l + s.string.split(",")

    for el in l :
        l[l.index(el)]= el.strip()

    print("list",l)

    return l

def reading_directory(text):
    import os
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from collections import Counter
    import re
    from nltk import defaultdict
    #fichier inverse avec dicionnaire
    dic_inverse= nltk.defaultdict(int)

    dic_inverse_string= nltk.defaultdict(nltk.defaultdict)

    from nltk import defaultdict


    documents = ""
    resultat=[]
    documents_list=""
    liste_of_dic=[]
    for f in os.listdir(text):


        documents =open(text+"/"+f,"r").read()
        documents=documents.lower()

        words=word_tokenize(documents,language='english',preserve_line='true')
        stopWords=set(stopwords.words('english'))
        liste=defaultdict(int)
        documents_list =  str(f)
        #print(documents_list)
        for w in words:

               if w not in stopWords:
                   s = re.match("[éçùàa-zA-z]+", w)
                   if  s:
                     # dic_inverse[w]=dic_inverse[w]+1
                       #liste[w]+=1
                       #if  documents_list not in dic_inverse_string[w]:
                      if f not in dic_inverse_string[w].keys():
                       dic_inverse_string[w][f]=0

                      dic_inverse_string[w][f] += 1

                     #liste.sort()

    #parcours du dictionnaire d'un fichier pour avoir frequence of each word
        #for el in liste:
          #  dic_inverse_string [el].append(str(dic_inverse_string[el])+str(liste[el])+";")


       # print(liste.items())
        #liste_of_dic.append(liste)
       # print(liste['said'])



        fm=open("resultat_inverse.txt","w")
        for i in dic_inverse_string:
            fm.write(i+":"+str(dic_inverse_string[i].items())+"\n")


        fm.close()
        for i in dic_inverse_string.keys():
            print(i,":",dic_inverse_string[i])
    return liste_of_dic

    #documents.write(dic_inverse_string.items())
   # print(dic_inverse_string.items())
    #print(dic_inverse['love'])


def Getwordsfromdocuements(document,fichierinverse):

    f=open(fichierinverse,"r").readlines()
    for line in f :
        if line.__contains__(document):
            print(line.split(":")[0],line.split(document+",")[1].split(";")[0])

def getdocumentsofword(word,fichierinverse):
    import re
    from nltk import  defaultdict
    f=open(fichierinverse,"r").readlines()
    dif_dj=nltk.defaultdic(int)
    for line in f:
        if re.match(word+":",line):
            liste=line.split(";")
            for el in liste:
                 doc_freq=el.split(",")
                 if  doc_freq.__len__()>1:
                      print(doc_freq[0],doc_freq[1])
                      dif_dj[doc_freq[0]]=doc_freq[1]

    return dif_dj
def calculni(fichierinverse,term):
    return len(getdocumentsofword(term,fichierinverse))

def calculfrequ(term,dj):
    liste =reading_directory("./TPRI")



    index=0
    frequence=[]
    Max=[]
    for i in liste :
       index+=1
       frequence = []
       for j in i:
            #print("document:",index,j ,i[j])
            frequence.append(i[j])
            print("document:",index,":",Max.append(frequence))

def calcul_poids(fichierinverse):
    import re
    from nltk import defaultdict
    f = open(fichierinverse, "r").readlines()
    dif_dj = nltk.defaultdic(int)
    for line in f:

            liste = line.split(";")
            for el in liste:
                doc_freq = el.split(",")
                if doc_freq.__len__() > 1:
                    print(doc_freq[0], doc_freq[1])
                    #dif_dj[doc_freq[0]] = doc_freq[1]












def calculidftf (listofdocument,fichierinverse):

    for i in listofdocument:
        for j in i:
            print("hi")



directory_creator(".","TPRI")

create_n_docuement("TPRI",1)
#emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#print("emma:",nltk.corpus.gutenberg.words('austen-emma.txt'))
#frequency_fichier("/home/masterubunto/PycharmProjects/RI/TPRI/hello.txt",stopwords(text="hi"))
import os
#reading_directory("./TPRI")
#calculfrequ("hello","j")
#calcul_poids("resultat.txt")
#Getwordsfromdocuements("austen-sense.txt","resultat_inverse.txt")
#getdocumentsofword("love","resultat_inverse.txt")
#f=open(os.path.abspath("TPRI")+"/austen-emma.txt","r").read()#
#calculni()
