from src import DataTable

def main():
    data = DataTable()

    data.generate(100,toDataFrame=True)

    data.fuzzyLogic(toDataFrame=True)

    data.printDataFrame()
    
if __name__ == "__main__":
    main()