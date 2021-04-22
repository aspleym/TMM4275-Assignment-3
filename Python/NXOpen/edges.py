# NX 1957
# Journal created by andreilo on Mon Apr 12 13:22:45 2021 W. Europe Daylight Time
from os import error
from os.path import expanduser
from Python.NXOpen.shapes.Block import Block
from Python.NXOpen.shapes.Line import Line
import math
import NXOpen


def main(part_path):

    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------

    # basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(
    #    "D:\\Dropbox\\Skole\\TMM4275 - Automatisering i ingeniørarbeid, prosjekt\\TMM4275-Assignment-3\\maze.prt", NXOpen.DisplayPartOption.AllowAdditional)

    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(
        part_path, NXOpen.DisplayPartOption.AllowAdditional)

    # basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(
    #    "C:\\Users\\Magnus\\Documents\\NX\\Models\\model15.prt", NXOpen.DisplayPartOption.AllowAdditional)

    workPart = theSession.Parts.Work  # maze
    displayPart = theSession.Parts.Display  # maze
    partLoadStatus1.Dispose()

    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------


def getFaces():
    theSession = NXOpen.Session.GetSession()
    # workPart = theSession.Parts.Work

    for i, partObject in enumerate(theSession.Parts):
        print("PART NUMBER: %i" % i)
        print(partObject.JournalIdentifier)
        if i == 0:
            processPart(partObject)


def processPart(partObject):
    for bodyObject in partObject.Bodies:
        # processBodyFaces(bodyObject)
        if bodyObject != baseBlock.body:
            try:
                print("Mag")
                print(bodyObject.JournalIdentifier)
                baseBlock.intersect(bodyObject)
                processEdge(bodyObject)
            except:
                print("Adr")


def processBodyFaces(bodyObject):
    for faceObject in bodyObject.GetFaces():
        processFace(faceObject)


def processFace(faceObject):
    print("Face found.")
    for edgeObject in faceObject.GetEdges():
        processEdge(edgeObject)


def processEdge(edgeObject):
    # Printing vertices
    v1 = edgeObject.GetVertices()[0]
    v2 = edgeObject.GetVertices()[1]
    print("Vertex 1:", v1)
    print("Vertex 2:", v2)


def getPotentialEdges(faces):
    potentialEdges = []
    for face in faces:
        for edge in face.GetEdges():
            v1 = edge.GetVertices()[0]
            v2 = edge.GetVertices()[1]
            if (v1.Z == 0 and v2.Z == 0):
                potentialEdges.append(edge)

    potentialEdges = list(dict.fromkeys(potentialEdges))

    return potentialEdges


# Sort edges in x and y direction. Return [x-edges], [y-edges]
def sortEdges(edges):
    x_edges = []
    y_edges = []
    for edge in edges:
        v1 = edge.GetVertices()[0]
        v2 = edge.GetVertices()[1]

        if (abs(v1.X - v2.X) < 0.01):
            y_edges.append(edge)
        else:
            x_edges.append(edge)
    return x_edges, y_edges

# Sort faces in x and y direction. Returns: [x-faces], [y-faces]
# Sort x and y arrays in acending order


def sortFaces(faces):
    x_faces = []
    y_faces = []
    z_faces = []
    counter = 0
    for face in faces:
        counter += 1
        x_sum = 0
        y_sum = 0
        z_sum = 0
        for edge in face.GetEdges():
            v1 = edge.GetVertices()[0]
            v2 = edge.GetVertices()[1]

            x_sum += abs(v1.X - v2.X)
            y_sum += abs(v1.Y - v2.Y)
            z_sum += abs(v1.Z - v2.Z)

        if (x_sum <= 0.01):
            y_faces.append(face)
        elif (y_sum <= 0.01):
            x_faces.append(face)
        elif (z_sum <= 0.01):
            z_faces.append(face)

    print("Number of faces checked: ", counter)
    print("Length of y-faces: ", len(y_faces))
    print("Length of x-faces: ", len(x_faces))

    x_faces = sorted(x_faces, key=lambda f: f.GetEdges()[0].GetVertices()[0].Y)
    y_faces = sorted(y_faces, key=lambda f: f.GetEdges()[0].GetVertices()[0].X)
    z_faces = sorted(z_faces, key=lambda f: f.GetEdges()[0].GetVertices()[0].Z)

    return x_faces, y_faces, z_faces


# Intersection between to rectangles. Input: target = {X1: 1, X2: 1, Y1: 1, Y2: 1}
# Returns boolean
def intersection(target, face, xdirecton):
    if (xdirecton):
        fVertices = []
        for edge in face.GetEdges():
            v1 = edge.GetVertices()[0]
            v2 = edge.GetVertices()[1]
            fVertices.append(v1)
            fVertices.append(v2)

        fX1 = min(fVertices, key=lambda p: p.Y).Y
        fX2 = max(fVertices, key=lambda p: p.Y).Y
        fY1 = min(fVertices, key=lambda p: p.Z).Z
        fY2 = max(fVertices, key=lambda p: p.Z).Z

        x1 = max(min(fX1, fX2),
                 min(target["X1"], target["X2"]))
        y1 = max(min(fY1, fY2),
                 min(target["Y1"], target["Y2"]))
        x2 = min(max(fX1, fX2),
                 max(target["X1"], target["X2"]))
        y2 = min(max(fY1, fY2),
                 max(target["Y1"], target["Y2"]))

        # NOT SURE HERE
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False
    else:
        fVertices = []
        for edge in face.GetEdges():
            v1 = edge.GetVertices()[0]
            v2 = edge.GetVertices()[1]
            fVertices.append(v1)
            fVertices.append(v2)

        fX1 = min(fVertices, key=lambda p: p.X).X
        fX2 = max(fVertices, key=lambda p: p.X).X
        fY1 = min(fVertices, key=lambda p: p.Z).Z
        fY2 = max(fVertices, key=lambda p: p.Z).Z

        x1 = max(min(fX1, fX2),
                 min(target["X1"], target["X2"]))
        y1 = max(min(fY1, fY2),
                 min(target["Y1"], target["Y2"]))
        x2 = min(max(fX1, fX2),
                 max(target["X1"], target["X2"]))
        y2 = min(max(fY1, fY2),
                 max(target["Y1"], target["Y2"]))

        # NOT SURE HERE
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False

# weldBotSize = [min-length, width, height]. Length will be along edge


def getFaceOfBotFromEdge(weldBotSize, edge, xdirection):
    # Check if there is a wide enough gap to fit the robot
    face1 = {}
    if xdirection:
        face1["X1"] = edge.GetVertices()[0].Y
        face1["Y1"] = edge.GetVertices()[0].Z
        face1["X2"] = face1["X1"] + weldBotSize[1]
        face1["Y2"] = face1["Y1"] + weldBotSize[2]
    else:
        face1["X1"] = edge.GetVertices()[0].X
        face1["Y1"] = edge.GetVertices()[0].Z
        face1["X2"] = face1["X1"] + weldBotSize[1]
        face1["Y2"] = face1["Y1"] + weldBotSize[2]

    return face1


def getWeldLines(partObject, weldBotSize):
    allFaces = []
    bottom = list(partObject.Bodies)[0]
    for body in list(partObject.Bodies):
        print("BODY:")
        body.Print()
        for feature in body.GetFeatures():
            feature.Print()
        for face in body.GetFaces():
            allFaces.append(face)
    x_faces, y_faces, z_faces = sortFaces(allFaces)
    potentialEdges = getPotentialEdges(allFaces)
    x_edges, y_edges = sortEdges(potentialEdges)
    quadrants = [[1, 1, 1], [1, -1, 1]]

    for edge in x_edges:
        edge.Print()
        x1 = min(edge.GetVertices()[0].X, edge.GetVertices()[1].X)
        x2 = max(edge.GetVertices()[0].X, edge.GetVertices()[1].X)

        for quadrant in quadrants:
            weldable = True
            bodyHit = []
            robot = [val * quadrant[i] for i, val in enumerate(weldBotSize)]
            target1 = getFaceOfBotFromEdge(robot, edge, True)
            robotInsideWall = False
            for face in y_faces:
                if abs(face.GetEdges()[0].GetVertices()[0].X - x2) <= 0.01:
                    if intersection(target1, face, True) and robotInsideWall:
                        weldable = False
                # TODO: Fix for when welding robot is bigger than edge
                if face.GetEdges()[0].GetVertices()[0].X < x1:
                    if intersection(target1, face, True):
                        print("<X intersecting: ", face.GetEdges())
                        if face.GetBody() not in bodyHit:
                            bodyHit.append(face.GetBody())
                        else:
                            bodyHit.remove(face.GetBody())
                if face.GetEdges()[0].GetVertices()[0].X > x1 and face.GetEdges()[0].GetVertices()[0].X < x2:
                    print("<X<: ", face.GetEdges()[0].GetVertices()[0].Y)
                    if intersection(target1, face, True):
                        weldable = False
                if face.GetEdges()[0].GetVertices()[0].X > x1 and len(bodyHit):
                    if intersection(target1, face, True):
                        weldable = False
                if abs(face.GetEdges()[0].GetVertices()[0].X - x1) <= 0.01:
                    if intersection(target1, face, True):
                        robotInsideWall = True

            if weldable:
                if (edge.GetBody() == bottom):
                    break
                line = Line(edge.GetVertices()[
                    0], edge.GetVertices()[1], weldable)
                line.initForNX()
                break

        if not weldable:
            if (edge.GetBody() != bottom):
                line = Line(edge.GetVertices()[
                    0], edge.GetVertices()[1], weldable)
                line.initForNX()

    for edge in y_edges:
        edge.Print()
        y1 = min(edge.GetVertices()[0].Y, edge.GetVertices()[1].Y)
        y2 = max(edge.GetVertices()[0].Y, edge.GetVertices()[1].Y)
        for quadrant in quadrants:
            weldable = True
            bodyHit = []
            robot = [val * quadrant[i] for i, val in enumerate(weldBotSize)]
            target1 = getFaceOfBotFromEdge(robot, edge, False)
            robotInsideWall = False
            for face in x_faces:
                if abs(face.GetEdges()[0].GetVertices()[0].Y - y2) <= 0.01:
                    if intersection(target1, face, False) and robotInsideWall:
                        weldable = False
                # TODO: Fix for when welding robot is bigger than edge
                if face.GetEdges()[0].GetVertices()[0].Y < y1:
                    if intersection(target1, face, False):
                        print("<Y intersecting: ", face.GetEdges()
                              [0].GetVertices()[0].Y)
                        if face.GetBody() not in bodyHit:
                            bodyHit.append(face.GetBody())
                        else:
                            bodyHit.remove(face.GetBody())

                if face.GetEdges()[0].GetVertices()[0].Y > y1 and face.GetEdges()[0].GetVertices()[0].Y < y2:
                    print("<Y<: ", face.GetEdges()[0].GetVertices()[0].Y)
                    if intersection(target1, face, False):
                        weldable = False

                if face.GetEdges()[0].GetVertices()[0].Y > y1 and len(bodyHit):
                    if intersection(target1, face, False):
                        weldable = False
                if abs(face.GetEdges()[0].GetVertices()[0].Y - y1) <= 0.01:
                    if intersection(target1, face, False):
                        robotInsideWall = True

            if weldable:

                if (edge.GetBody() == bottom):
                    break

                line = Line(edge.GetVertices()[
                    0], edge.GetVertices()[1], weldable)
                line.initForNX()

                break
        if not weldable:
            if (edge.GetBody() != bottom):
                line = Line(edge.GetVertices()[
                    0], edge.GetVertices()[1], weldable)
                line.initForNX()

# path C:\\, and [50, 50, 50]


def runWC(part_path, weldbot):
    main(part_path)

    for i, partObject in enumerate(theSession.Parts):
        print("PART NUMBER: %i" % i)
        print(partObject.JournalIdentifier)
        if i == 0:
            getWeldLines(partObject, weldbot)

            try:
                print("Saving .prt file.")
                # partObject.Save()
                print("Success!")
            except:
                print("Could not save .prt file.")


if __name__ == '__main__':
    main()

    theSession = NXOpen.Session.GetSession()
    for i, partObject in enumerate(theSession.Parts):
        print("PART NUMBER: %i" % i)
        print(partObject.JournalIdentifier)
        if i == 0:
            getWeldLines(partObject, [50, 50, 50])
