from src import DataTable

def main():
    data = DataTable()

    print(data.generate(10,toDataFrame=True))

    data.printDataFrame()



    
    

if __name__ == "__main__":
    main()