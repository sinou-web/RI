#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:26:31 2018

@author: izan
"""

import sys
#from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import QApplication,QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
from operator import itemgetter
import nltk, os, FichierInverse,ModeleVect, ModeleBool, ModeleProba
DIR = "./TPRI"
N = len(os.listdir(DIR)) #nbr de docs

class TestApp(Ui_MainWindow):


    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        
        
        
        self.DisplayInvFile.clicked.connect(self.FDisplayInvFile)
        self.DisplayWInvFile.clicked.connect(self.FDisplayWInvFile)
        self.ModeleBool_2.clicked.connect(self.FDisplayDocs)
        self.ModeleBool_3.clicked.connect(self.FDisplayTermes)
        self.ModeleBool.clicked.connect(self.FModeleBool)
        self.ModeleVect.clicked.connect(self.FModeleVect)
        self.ech.clicked.connect(self.RemplirEchantillon)
        self.ModeleProba.clicked.connect(self.FModeleProba)
        
        
        
        
    """ ******************* affichage fichier inverse **************** """    

    def FDisplayInvFile(self):
#        self.tableWidgetInvFile.clear()
        self.tableWidgetInvFile.setRowCount(0);
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)

        Termes = list(fichierInverse.keys())
        Fichiers = list(os.listdir(DIR))
         
        # Create a empty row at bottom of table
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)
        
        # Add the files name
        i=0
        for f in Fichiers:
            self.tableWidgetInvFile.setItem(numRows,i+1 , QtWidgets.QTableWidgetItem(f))
            i= i+1
            
        for terme in Termes:            
            self.AddRowInvFile(terme,fichierInverse,Fichiers)


    def AddRowInvFile(self,terme,fichierInverse,Fichiers):
        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)
                    
        # Add text to the row
        self.tableWidgetInvFile.setItem(numRows,0 , QtWidgets.QTableWidgetItem(terme))
        for j in range(len(Fichiers)):
            if Fichiers[j] in list(fichierInverse[terme].keys()):
                val = str(fichierInverse[terme][Fichiers[j]])
            else:
                val = "0"

            self.tableWidgetInvFile.setItem(numRows, j+1 , QtWidgets.QTableWidgetItem(val))
            
    
    """ ******************* affichage fichier inverse des Poids **************** """    


            
    def FDisplayWInvFile(self):
        self.tableWidgetInvFile.setRowCount(0);
        
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        fichierInverse = FI.tfidf(fichierInverse,N)

        Termes = list(fichierInverse.keys())
        Fichiers = list(os.listdir(DIR))
         
        # Create a empty row at bottom of table
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)
        
        # Add the files name
        i=0
        for f in Fichiers:
            self.tableWidgetInvFile.setItem(numRows,i+1 , QtWidgets.QTableWidgetItem(f))
            i= i+1
            
        for terme in Termes:            
            self.AddRowInvFile(terme,fichierInverse,Fichiers)




        """ ************************* liste des docs pour un terme ********************"""
    
    def FDisplayDocs(self):
        self.tableWidgetDocs.setRowCount(0);
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        fichierInverseW = FI.tfidf(fichierInverse,N)
        
        word = self.reqBool_2.text()
        ListDocsF = FI.getDocsOfWordFreq(word,fichierInverse)
        ListDocsP = FI.getDocsOfWordPoids(word,fichierInverseW)
        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetDocs.rowCount()
        self.tableWidgetDocs.insertRow(numRows)
        
        for item in ListDocsF:
            self.tableWidgetDocs.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidgetDocs.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(ListDocsF.get(item))))
            self.tableWidgetDocs.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(ListDocsP.get(item))))
            numRows = self.tableWidgetDocs.rowCount()
            self.tableWidgetDocs.insertRow(numRows)
            
            
        """ ************************* liste des docs pour un terme ********************"""
    
    def FDisplayTermes(self):
        self.tableWidgetTermes.setRowCount(0);
        
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        fichierInverseW = FI.tfidf(fichierInverse,N)
        
        doc = self.reqBool_3.text()
        ListTersF = FI.getWordsOfDocFreq(doc,fichierInverse)
        ListTersP = FI.getWordsOfDocPoids(doc,fichierInverseW)
        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetTermes.rowCount()
        self.tableWidgetTermes.insertRow(numRows)
        
        for item in ListTersF:
            self.tableWidgetTermes.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidgetTermes.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(ListTersF.get(item))))
            self.tableWidgetTermes.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(ListTersP.get(item))))
            numRows = self.tableWidgetTermes.rowCount()
            self.tableWidgetTermes.insertRow(numRows)
            
            
            
        """ ************************* modele Boolean ********************"""
    
    def FModeleBool(self):
        self.tableWidgetDocsBool.setRowCount(0);
        
        MB = ModeleBool.Boolean()
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        
        req = self.reqBool.text()
        ListDocs = MB.modeleBoolean(DIR,fichierInverse, req)

        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetDocsBool.rowCount()
        self.tableWidgetDocsBool.insertRow(numRows)
        
        for item in ListDocs:
            self.tableWidgetDocsBool.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item))
            numRows = self.tableWidgetDocsBool.rowCount()
            self.tableWidgetDocsBool.insertRow(numRows)
        
            
    """ ************************* modele Vectoriel ********************"""
    
    def FModeleVect(self):
        self.tableWidgetDocsVect.setRowCount(0);
        
        MV = ModeleVect.Vectoriel()
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        
        req = self.reqVect.text()
        choix = str(self.comboBox.currentText())
        
        ListDocs = MV.modeleVect(DIR,fichierInverse, req,choix)

        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetDocsVect.rowCount()
        self.tableWidgetDocsVect.insertRow(numRows)
        
        for item in ListDocs:
            self.tableWidgetDocsVect.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item[0]))
            self.tableWidgetDocsVect.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            numRows = self.tableWidgetDocsVect.rowCount()
            self.tableWidgetDocsVect.insertRow(numRows)
    

    """ ********************** Modele Probabiliste *********************** """
    def FModeleProba(self):
        self.tableWidgetDocsProba.setRowCount(0);
        
        MP = ModeleProba.Proba()
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        fichierPoids = FI.tfidf(fichierInverse,N)

        Fichiers = list(os.listdir(DIR))
        
        req = self.reqProba.text()
        choix = str(self.comboBoxProba.currentText())
        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetDocsProba.rowCount()
        self.tableWidgetDocsProba.insertRow(numRows)
        
        
        if choix == "Avec echantillon":
            listProbaDoc1 = []
            for doc in Fichiers:
                R = self.getNbrDocPertinant_R()
                ListDoc = self.getSelectedItem()

                sim = MP.ProbaAvecEch(N,doc,fichierPoids,fichierInverse,Fichiers,req,R,ListDoc)
                if sim > 0:
                    listProbaDoc1.append((doc,sim))
                
                listProbaDoc1 = sorted(listProbaDoc1, key=itemgetter(1),reverse=True)
                
                
            for (doc,sim) in listProbaDoc1:
                self.tableWidgetDocsProba.setItem(numRows, 0, QtWidgets.QTableWidgetItem(doc))
                self.tableWidgetDocsProba.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(sim)))
                numRows = self.tableWidgetDocsProba.rowCount()
                self.tableWidgetDocsProba.insertRow(numRows)
                    
        if choix == "Sans echantillon":
            listProbaDoc2 = []
            for doc in Fichiers:
                sim = MP.ProbaSansEch(N,doc,fichierPoids, fichierInverse, Fichiers, req)
                if sim > 0:
                    listProbaDoc2.append((doc,sim))
                
            listProbaDoc2 = sorted(listProbaDoc2, key=itemgetter(1),reverse=True)

                
            for (doc,sim) in listProbaDoc2:
                self.tableWidgetDocsProba.setItem(numRows, 0, QtWidgets.QTableWidgetItem(doc))
                self.tableWidgetDocsProba.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(sim)))
                numRows = self.tableWidgetDocsProba.rowCount()
                self.tableWidgetDocsProba.insertRow(numRows)
                    
        if choix == "BM25":
            listProbaDoc3 = list()
            for doc in Fichiers:
                sim=MP.ProbaBM25(N,doc,fichierPoids, fichierInverse, Fichiers, req)
                if sim > 0:
                    listProbaDoc3.append((doc,sim))
                
            listProbaDoc3 = sorted(listProbaDoc3, key=itemgetter(1),reverse=True)
                
            for (doc,sim) in listProbaDoc3:
                self.tableWidgetDocsProba.setItem(numRows, 0, QtWidgets.QTableWidgetItem(doc))
                self.tableWidgetDocsProba.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(sim)))
                numRows = self.tableWidgetDocsProba.rowCount()
                self.tableWidgetDocsProba.insertRow(numRows)
        
        

    def RemplirEchantillon(self):
        MV = ModeleVect.Vectoriel()
        FI = FichierInverse.FichierInverse()
        fichierInverse = FI.reading_directory(DIR)
        
        req = self.reqProba.text()
        choix = "Produit Interne" #str(self.comboBox.currentText())
        
        ListDocs = MV.modeleVect(DIR,fichierInverse, req,choix)
        
        
        # Create a empty row at bottom of table
        self.tableWidgetEch.setRowCount(0);
        numRows = self.tableWidgetEch.rowCount()
        self.tableWidgetEch.insertRow(numRows)
        
        for item in ListDocs:
            self.tableWidgetEch.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item[0]))
            numRows = self.tableWidgetEch.rowCount()
            self.tableWidgetEch.insertRow(numRows)
#        Fichiers = list(os.listdir(DIR))
#
#        self.tableWidgetEch.setRowCount(0);
#        numRows = self.tableWidgetEch.rowCount()
#        self.tableWidgetEch.insertRow(numRows)
#            
#        for item in Fichiers:
#            self.tableWidgetEch.setItem(numRows, 0, QtWidgets.QTableWidgetItem(item))
#            numRows = self.tableWidgetEch.rowCount()
#            self.tableWidgetEch.insertRow(numRows)
        
        
    def getSelectedItem(self):
        SelectedDocs = []
        Liste = self.tableWidgetEch.selectedItems()
        for item in Liste:
            SelectedDocs.append(int(self.tableWidgetEch.row(item)))
       
        return SelectedDocs
    
    
    def getNbrDocPertinant_R(self):
        return len(self.getSelectedItem())
    

            
            
            

            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()

    interface = TestApp(dialog)

    dialog.show()
    sys.exit(app.exec_())