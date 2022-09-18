import csv

class read_data:
    def __init__(self):
       pass



    def getTestcaseData(self,filename: str, testcase_name: str) -> dict:
        data = {}
        list_key = []
        list_value = []
        found = False
        key_found = False
        with open(filename, mode='r', ) as file:
            # reading the CSV file
            self.csvFile = csv.reader(file, delimiter=',')
            row_index = 0
            key_index = 0
            done = False
            for row in self.csvFile:
                if done and len(row) == 0:
                    break
                row_index = row_index + 1
                if len(row) != 0:
                    if found:
                        for index in range(len(row)):
                            if len(row) != len(list_key):
                                list_key.append(row.__getitem__(index))
                                key_index = row_index
                    if key_index < row_index and found and len(row) != 0:
                        for index in range(len(row)):
                            if len(row) != len(list_value):
                                list_value.append(row.__getitem__(index))
                        done = True
                    if testcase_name == row[0]:
                        found = True
            if len(list_value) == len(list_key):
                for index in range(len(list_key)):
                    data.__setitem__(list_key[index],list_value[index])
            return data






