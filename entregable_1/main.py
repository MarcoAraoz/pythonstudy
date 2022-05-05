import pandas as pd
import glob

class ConcatFile:
    def __init__(self, extension):
        """
        It takes a file extension as an argument and returns a list of all the files in the current
        directory that have that extension
        
        :param extension: The extension of the files you want to merge
        """
        self.csv_files = glob.glob(f"*.{extension}")
        self.li_csv = []

    def readFile(self):
        """
        It reads in a list of csv files, concatenates them into a single dataframe, and returns the
        dataframe
        :return: The dataframe
        """
        for filename in self.csv_files:
            self.df = pd.read_csv(filename, index_col=None, header=0)
            self.li_csv.append(self.df)
        self.frame = pd.concat(self.li_csv, axis=0, ignore_index=True)
        return self.frame


# It reads a file, combines the first and last name columns, replaces spaces with underscores, and
# makes everything lowercase
class CreateTable(ConcatFile):
    def __init__(self, extension):
        """
        It reads the file and returns the dataframe
        
        :param extension: The extension of the file you want to read
        """
        super().__init__(extension)
        self.frame = self.readFile()

    def getFullName(self):
        """
        It takes the first and last name columns, combines them, replaces spaces with underscores, and makes
        everything lowercase
        """
        self.frame = self.frame.fillna("%")
        self.frame["Full Name"] = (
            (self.frame["First Name"] + " " + self.frame["Last Name"])
            .str.replace(" ", "_")
            .str.lower()
        )
        self.frame = self.frame[["Full Name", "Accuracy", "Score"]]
        self.frame = self.frame.sort_values("Full Name")


# It takes a csv file, reads it, and then prints the top 5 users with the highest score
class FindBestUsers(CreateTable):
    def __init__(self, extension):
        super().__init__(extension)
        self.list_users = {}

    def addedPoints(self):
        for index, row in self.frame.iterrows():
            if row["Full Name"] in self.list_users.keys():
                self.list_users[row["Full Name"]] += row["Score"]
            else:
                self.list_users[row["Full Name"]] = row["Score"]

    def printUsers(self, max_lenght):

        self.myList = zip(self.list_users, self.list_users.values())

        self.myList = list(self.myList)

        self.myList.sort(key=lambda x: -x[1])
        print(self.myList[0:max_lenght])


prueba = FindBestUsers("csv")

prueba.readFile()
prueba.getFullName()
prueba.addedPoints()
prueba.printUsers(4)