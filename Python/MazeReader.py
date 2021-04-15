import pandas as pd
import os


def readCsv(fileName):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../Maze/Uploaded/' + fileName)
    print(filename)

    df = pd.read_csv(filename, index_col=None, header=None, sep=';')
    data = df.values

    return data


def writeCsv(data):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../Maze/Basic2.csv')
    df = pd.DataFrame(data)
    df.to_csv(filename, sep=';')
