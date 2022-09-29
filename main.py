import csv, random, numpy
from collections import defaultdict
from itertools import product

Browsers = ["Chrome", "Firefox", "Edge"]
PP = ["None", "Standard", "Strict"]
experiment = {}


def read_and_shuffle(file):
    columns = defaultdict(list)  # each value in each column is appended to a list
    global top27
    top27 = []
    with open(file) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k
    for i in range(27):
        top27.append(columns['Websites'][i])

    random.shuffle(top27)
    return top27



if __name__ == "__main__":
    top27 = read_and_shuffle("tranco-list.csv")
    l = list(numpy.array_split(top27, 9))
    keylist = list(product(Browsers, PP))
    for i in range(9):
        experiment[keylist[i]] = l[i]
    print(experiment)
