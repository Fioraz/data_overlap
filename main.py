with open("file1.txt") as datafile_1:
    data_1 = datafile_1.readlines()

with open("file2.txt") as datafile_2:
    data_2 = datafile_2.readlines()

# print(data_2)
new_list = [int(x) for x in data_1 if x in data_2]
print(new_list)