from faker import Faker

import pandas as pd
import numpy as np
import os
import uuid


class DataTable:

    def __init__(self):
        """"Class for create a table to measure a student's reward for scholarship"""

        # create a data variable to store student data
        self.dataMhs : list = []

        # create a object variable to create a fake data from faker module
        self.faker : Faker = Faker("id_ID")

        # create a variable to store a fuuzy base result from dataMhs
        self.dataFuzzy : list = []

        # a variable to store pandas's dataFrame from stundet's data
        self.dataMhsFrame : pd.DataFrame = None

        # a variable to store pandas's dataFrame from stundet's fuzzy logic result
        self.dataFuzzyFrame : pd.DataFrame = None

    def generate(self,genNum : int, toDataFrame : bool = False):
        """"Generate A Data base on user input"""

        # IPK score variant
        score = np.arange(1,4.01,0.01)

        # Salary variant
        gaji = np.arange(1,10,0.5)

        # both how many sibling and child parent have variant
        tanggunganAndKandung = np.arange(1,6,1)

        # make a loop on base on user input
        for i in range(genNum):
            # append data from index,name,id,IPK,salary,child,sibling
            self.dataMhs.append([i + 1, self.faker.name(),uuid.uuid4(),np.random.choice(score), np.random.choice(gaji), np.random.choice(tanggunganAndKandung), np.random.choice(tanggunganAndKandung)])

        # generate to pandas Frame id user set it to true
        if toDataFrame :
            # generate dataframe inclde number of index,name,ID,IPK,salary,child,sibling
            self.dataMhsFrame = pd.DataFrame(self.dataMhs, columns=["No", "Nama","ID", "IPK", "Gaji (jt)", "Jumlah Tanggungan Ortu", "Jumlah Saudara kandung"]).set_index("No")

        return self.dataMhs
    
    def fetchData(self, dirData = None):
        """"If the data already generate or the data already exist fetch will get the data,
        an exception is that the data has to be a xlsx or xls data and already fill with column of
        "No", "Nama","ID", "IPK", "Gaji (jt)", "Jumlah Tanggungan Ortu", "Jumlah Saudara kandung."""

        # check if the user input the directory
        if dirData == None:
            # if the user did not input the directory then raise an error
            raise Exception("Please insert the directory of the data, the data cannot be empty")

        # Read the data
        self.dataMhsFrame = pd.read_excel(dirData)

        # convert the data into list
        self.dataMhs = self.dataMhsFrame.values.tolist()

        return self.dataMhs

    
    def printDataFrame(self, directory = None):
        try:
            # print the data frame 
            if directory == None:
                # if directory not set by user the default directory will be in the main directory
                if "excel" not in os.listdir("./"):
                    # if the excel has not been made before program will make it first before store it.
                    os.mkdir("excel")
                    self.dataMhsFrame.to_excel("excel/Masukan.xlsx", sheet_name="Sheet1")
                    self.dataFuzzyFrame.to_excel("excel/Luaran.xlsx", sheet_name="Sheet1")
                else:
                    # if the excel already made the program will update the file
                    self.dataMhsFrame.to_excel("excel/Masukan.xlsx", sheet_name="Sheet1")
                    self.dataFuzzyFrame.to_excel("excel/Luaran.xlsx", sheet_name="Sheet1")
            else:
                # if the user set the directory that dirextory will be use instead
                self.dataMhsFrame.to_excel(f'{directory}/Masukan.xlsx', sheet_name="Sheet1")
                self.dataFuzzyFrame.to_excel(f'{directory}/Luaran.xlsx', sheet_name="Sheet1")
        except Exception as e:
            # if any error exist print the error
            print(f'{e}')
    
    def fuzzyLogic(self, toDataFrame : bool = False):
        """"Fuzzy logic Multiple Atrribute Decision Making, the fungsion decide which of the colleage student deserve to have scholarship"""

        # If the data has not been made retutn imideadly
        if len(self.dataMhs) < 0 :
            return

        # IPK Weight on matrix
        ipk = 0

        # Salary weight on matrix
        gaji = 0

        # Child responsible weight on matrix
        tang = 0

        # sibline weight on matrix
        kand = 0

        # Create a matrix weight on each atribute
        for idx,val in enumerate(self.dataMhs):
            tempIPK = 0
            tempGaji = 0
            tempTang = 0
            tempKand = 0

            if val[3] <= 2.75:
                tempIPK = 0
            elif val[3] > 2.75 and val[3] <= 3.00:
                tempIPK = 0.25
            elif val[3] > 3.00 and val[3] <= 3.25:
                tempIPK = 0.5
            elif val[3] > 3.25 and val[3] <= 3.50:
                tempIPK = 0.75
            elif val[3] > 3.50:
                tempIPK = 1.00
            
            if val[4] <= 1:
                tempGaji = 0.25
            elif val[4] > 1.00 and val[4] <= 5.00:
                tempGaji = 0.5
            elif val[4] > 5.00 and val[4] <= 10.00:
                tempGaji = 0.75
            elif val[4] > 10.00:
                tempGaji = 1.00

            if val[5] == 1:
                tempTang = 0
            elif val[5] == 2:
                tempTang = 0.25
            elif val[5] == 3:
                tempTang = 0.5
            elif val[5] == 4:
                tempTang = 0.75
            else:
                tempTang = 1

            if val[6] == 1:
                tempKand = 0
            elif val[6] == 2:
                tempKand = 0.25
            elif val[6] == 3:
                tempKand = 0.5
            elif val[6] == 4:
                tempKand = 0.75
            else:
                tempKand = 1
            
            ipk += tempIPK
            gaji += tempGaji
            tang += tempTang
            kand += tempKand

        # an average of to create the weight
        ipk = ipk / len(self.dataMhs)
        gaji = gaji / len(self.dataMhs)
        tang = tang / len(self.dataMhs)
        kand = kand / len(self.dataMhs)
        
        # decide on deservve point on each student
        for idx,val in enumerate(self.dataMhs):
            tempIPK = 0
            tempGaji = 0
            tempTang = 0
            tempKand = 0

            # IPK
            if val[3] <= 2.75:
                tempIPK = 0
            elif val[3] > 2.75 and val[3] <= 3.00:
                tempIPK = 0.25
            elif val[3] > 3.00 and val[3] <= 3.25:
                tempIPK = 0.5
            elif val[3] > 3.25 and val[3] <= 3.50:
                tempIPK = 0.75
            elif val[3] > 3.50:
                tempIPK = 1.00
            
            # Gaji
            if val[4] <= 1:
                tempGaji = 1
            elif val[4] > 1.00 and val[4] <= 5.00:
                tempGaji = 0.75
            elif val[4] > 5.00 and val[4] <= 10.00:
                tempGaji = 0.5
            elif val[4] > 10.00:
                tempGaji = 0.25

            # Tanggungan
            if val[5] == 1:
                tempTang = 0
            elif val[5] == 2:
                tempTang = 0.25
            elif val[5] == 3:
                tempTang = 0.5
            elif val[5] == 4:
                tempTang = 0.75
            else:
                tempTang = 1

            # Saudara Kandung
            if val[6] == 1:
                tempKand = 0
            elif val[6] == 2:
                tempKand = 0.25
            elif val[6] == 3:
                tempKand = 0.5
            elif val[6] == 4:
                tempKand = 0.75
            else:
                tempKand = 1

            # include a number, name, ID, NK(Nilai Kelayakan)
            self.dataFuzzy.append([val[0], val[1], val[2], ((tempIPK * ipk) + (tempGaji * gaji) + (tempTang * tang) + (tempKand * kand))])
        
        # if the user set to true the it will be set into pandas data frame
        if toDataFrame:
            # convert the data into pandas dataFrame
            self.dataFuzzyFrame = pd.DataFrame(self.dataFuzzy, columns=["No", "Nama", "ID", "NK"]).set_index("No").sort_values(['NK'], ascending=False)

            # create a index number based on the data length
            index = np.arange(1,len(self.dataMhsFrame) + 1)

            # change the values of the index
            self.dataFuzzyFrame.index = index

            # change the index's label
            self.dataFuzzyFrame.index.name = "No"

        return self.dataFuzzy
