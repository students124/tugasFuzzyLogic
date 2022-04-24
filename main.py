from src import DataTable

def main():
    # Create an object of class Data tabel
    data = DataTable()

    # Generate an data base on input
    data.generate(100, toDataFrame=True)

    # use fuzzy logic to solve the problem on the data
    data.fuzzyLogic(toDataFrame=True)

    # Print the data into xlsx
    data.printDataFrame()
    
if __name__ == "__main__":
    main()