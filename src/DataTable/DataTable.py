import pandas as pd
import numpy as np
import os
import uuid


class DataTable:

    def __init__(self):
        self.dataMhs : list = []
        self.dataMhsFrame : pd.DataFrame = None

    def generate(self,genNum : int, toDataFrame : bool = False):
        score = np.arange(0,4.01,0.01)
        gaji = np.arange(1,10,0.5)

        for i in range(genNum + 1):
            self.dataMhs.append([i + 1, uuid.uuid4(),np.random.choice(score), np.random.choice(gaji)])

        if toDataFrame :
            self.dataMhsFrame = pd.DataFrame(self.dataMhs, columns=["No", "Mahasiswa ID", "Score", "Gaji"]).set_index("No")

        return self.dataMhs
    
    def printDataFrame(self, directory = None):
        try:
            #print
            if directory == None:
                if "excel" not in os.listdir("./"):
                    os.mkdir("excel")
                    self.dataMhsFrame.to_excel("excel/Data.xlsx", sheet_name="Sheet1")
                else:
                    self.dataMhsFrame.to_excel("excel/Data.xlsx", sheet_name="Sheet1")
            else:
                self.dataMhsFrame.to_excel(f'{directory}/Data.xlsx', sheet_name="Sheet1")
        except Exception as e:
            print(f'{e}')
        
    

