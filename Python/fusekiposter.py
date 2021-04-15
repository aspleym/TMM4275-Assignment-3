import requests

def postTrajectory(name, trajectory):

    points = "\n "
    pointNames = ""
    for i, t in enumerate(trajectory):
        if i != 0:
            pointNames += ', '
        points += f'kbe:P{name}{i} a owl:NamedIndividual, kbe:Point;\n        kbe:x\t"{t[0]}"^^xsd:integer;\n        kbe:y   "{t[1]}"^^xsd:integer;\n        kbe:index "{i}"^^xsd:integer.\n\n '
        pointNames += f'kbe:P{name}{i}'
    pointNames += '.'

    headers = {
    'Accept': 'text/plain,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  INSERT\n  {\n'
    info = f'\tkbe:Traj{name} a owl:NamedIndividual, kbe:Trajectory;\n    \tkbe:Points kbe:Points{name}.\n\t\n    kbe:Points{name} a owl:NamedIndividual, kbe:Points;\n    \tkbe:Point\t{pointNames}\n  \n  \t{points}\n'
    postfix = '}\nwhere {}'
    data = {
        'update': prefix + info + postfix
    }

    response = requests.post('http://127.0.0.1:3030/kbe', headers=headers, data=data)

def getTrajectory(name):

    headers = {
    'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }

    prefix = 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nPREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  SELECT *\n  WHERE\n  {\n'

    info = f' ?trajectory a kbe:Trajectory.\n  ?trajectory kbe:Points ?points.\n\t?points kbe:Point ?point.\n  ?point kbe:index ?index.\n    ?point kbe:x ?x.\n    ?point kbe:y ?y.\nFILTER(?trajectory = kbe:Traj{name}).'
    postfix = '\n  } '
    data = {
        'query': prefix + info + postfix
    }
    response = requests.post('http://127.0.0.1:3030/kbe', headers=headers, data=data)

    jsonResponse = response.json()

    return jsonResponse
