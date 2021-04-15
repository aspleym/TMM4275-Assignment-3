import os
import requests
import json
from Python.Maze import Maze
from Python.MazeReader import readCsv
from Python.fusekiposter import getTrajectory

#! THIS FUNCTION GENERATES A DFA WITH BOTH A MAZE AND TRAJECTORY FROM CSV

def getIndex(elem):
    return elem[2]

def generateDFA(fileName):
    # Request trajectory data from Fuseki-server
    data = getTrajectory(fileName.removesuffix(".csv"))

    mazeData = readCsv(fileName)

    blocks = ""

    height = mazeData.shape[0]
    width = mazeData.shape[1]
    

    for i in range(height):
        for j in range(width):
            if (mazeData[i, j] == -1):
                blocks = blocks + f'Point({i - 0.5}, {j - 0.5}, 0),\n'
   
    trajectoryData = []

    for p in data['results']['bindings']:
        x = int(p['x']['value'])
        y = int(p['y']['value'])
        index = int(p['index']['value'])

        trajectoryData.append((x, y, index))

    trajectoryData.sort(key=getIndex)

    trajectory = ""

    for p in trajectoryData:
        trajectory = trajectory + f'Point({p[0]}, {p[1]}, 2.5),\n'

    trajectory = trajectory.removesuffix(",\n")

    blocks = blocks.removesuffix(",\n")
    trajectory = trajectory.removesuffix(",\n")

    script_dir = os.path.dirname(__file__)
    rel_path_template = "DFA/MazeAndTrajectoryTemplate.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_template)

    resultFileName = fileName.removesuffix(".csv")
    f = open(abs_file_path_template, "r")
    txt = f.read()

    # Replacement section for parameters in the template file
    txt = txt.replace("<T_NAME>", resultFileName)

    txt = txt.replace("<BLOCK_POINTS>", blocks)
    txt = txt.replace("<TRAJECTORY_POINTS>", trajectory)

    rel_path_product = f'DFA/products/{resultFileName}.dfa'
    abs_file_path_product = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_product)

    f = open(abs_file_path_product, "w")
    f.write(txt)
    f.close()
    

def generateMaze(fileName):

    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  SELECT *\n  WHERE\n  {\n  ?trajectory a kbe:Trajectory.\n  ?trajectory kbe:Points ?point.\n  ?point kbe:index ?index.\n    ?point kbe:x ?x.\n    ?point kbe:y ?y.   \n    FILTER(?trajectory = kbe:'
    postfix = ').\n}'
    data = {
    'query': prefix + tName + postfix
    }

    response = requests.post('http://127.0.0.1:3030/kbe', headers=headers, data=data)
    data = response.json()

    points = ""

    for point in data['results']['bindings']:
        x = int(point['x']['value'])
        y = int(point['y']['value'])
        index = int(point['index']['value'])

        points = points + f'Point({x}, {y}, 0),\n'

    points = points.removesuffix(",\n")

    m = Maze(fileName)
    data = readCsv(fileName)
    blocks = ""
    trajectory = ""

    height = data.shape[0]
    width = data.shape[1]

    for i in range(height):
        for j in range(width):
            if (data[i, j] == -1):
                blocks = blocks + f'Point({i - 0.5}, {j - 0.5}, 0),\n'
    
    for p in m.trajectory:
        trajectory = trajectory + f'Point({p[0]}, {p[1]}, 2.5),\n'


    blocks = blocks.removesuffix(",\n")
    trajectory = trajectory.removesuffix(",\n")

    script_dir = os.path.dirname(__file__)
    rel_path_template = "DFA/MazeAndTrajectoryTemplate.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_template)

    mazeName = fileName.removesuffix(".csv") + "MAZE"
    f = open(abs_file_path_template, "r")
    txt = f.read()

    # Replacement section for parameters in the template file
    txt = txt.replace("<T_NAME>", mazeName)

    txt = txt.replace("<BLOCK_POINTS>", blocks)
    txt = txt.replace("<TRAJECTORY_POINTS>", trajectory)

    rel_path_product = f'DFA/products/{mazeName}.dfa'
    abs_file_path_product = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_product)

    f = open(abs_file_path_product, "w")
    f.write(txt)
    f.close()
    

def generateTrajectory(tName):
    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  SELECT *\n  WHERE\n  {\n  ?trajectory a kbe:Trajectory.\n  ?trajectory kbe:Points ?point.\n  ?point kbe:index ?index.\n    ?point kbe:x ?x.\n    ?point kbe:y ?y.   \n    FILTER(?trajectory = kbe:'
    postfix = ').\n}'
    data = {
    'query': prefix + tName + postfix
    }

    response = requests.post('http://127.0.0.1:3030/kbe', headers=headers, data=data)
    data = response.json()

    points = ""

    for point in data['results']['bindings']:
        x = int(point['x']['value'])
        y = int(point['y']['value'])
        index = int(point['index']['value'])

        points = points + f'Point({x}, {y}, 0),\n'

    points = points.removesuffix(",\n")
    
    script_dir = os.path.dirname(__file__)
    rel_path_template = "DFA/TrajectoryTemplate.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_template)

    f = open(abs_file_path_template, "r")
    txt = f.read()

    # Replacement section for parameters in the template file
    txt = txt.replace("<T_NAME>", tName)

    txt = txt.replace("<TRAJECTORY_POINTS>", points)

    rel_path_product = f'DFA/products/{tName}.dfa'
    abs_file_path_product = os.path.join(
        script_dir[:len(script_dir) - 6], rel_path_product)

    f = open(abs_file_path_product, "w")
    f.write(txt)
    f.close()
