from Python.MazeReader import readCsv, writeCsv


class Maze:

    def __init__(self, fileName):
        self.data = readCsv(fileName)
        self.height = self.data.shape[0]

        self.width = self.data.shape[1]

        self.startPos = (0, 0)  # self.getStartPos()

        self.mapEdges()

        self.trajectory = [self.startPos]

    def getStartPos(self):
        for i in range(self.height):
            for j in range(self.width):
                if (self.data[i, j] == 0):
                    return (i, j)

    def getNeighbours(self, pos, data):
        neighbours = []

        for x in [-1, 1]:
            if (pos[1]+x < 0 or pos[1]+x >= self.width):
                continue
            neighbours.append(
                [[pos[0], pos[1]+x], data[pos[0], pos[1]+x]])

        for y in [-1, 1]:
            if (pos[0]+y < 0 or pos[0]+y >= self.height):
                continue
            neighbours.append(
                [[pos[0]+y, pos[1]], data[pos[0]+y, pos[1]]])

        # FORMAT array[[row, col], value]
        # print(neighbours)
        return neighbours

    def getAllNeighbours(self, pos):
        neighbours = []

        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if (x == 0 and y == 0):
                    continue

                if (pos[0]+y < 0 or pos[0]+y >= self.height):
                    continue

                if (pos[1]+x < 0 or pos[1]+x >= self.width):
                    continue

                neighbours.append(
                    [[pos[0]+y, pos[1]+x], self.data[pos[0]+y, pos[1]+x]])

        # FORMAT array[[row, col], value]
        return neighbours

    def mapEdges(self):
        for i in range(self.height):
            for j in range(self.width):
                for n in self.getAllNeighbours((i, j)):
                    if (n[1] == -1 and self.data[i, j] != -1):
                        # Defines a point that should be welded
                        self.data[i, j] = 3

    def getWeldLine(self):
        startPos = self.trajectory[-1]
        neigh = self.getNeighbours(startPos, self.data)
        self.data[startPos] = 4

        while (len(list(filter(lambda x: (x[1] == 3), neigh))) > 0):
            weldPoints = list(filter(lambda x: (x[1] == 3), neigh))
            bestNumNeigh = -1  # Sum of 4's and -1's
            bestPoint = None
            for p in weldPoints:
                numNeigh = 0
                neigh = self.getAllNeighbours(p[0])
                for n in neigh:
                    if (n[1] == -1 or n[1] == 4):
                        numNeigh += 1

                if numNeigh > bestNumNeigh:
                    bestNumNeigh = numNeigh
                    bestPoint = p[0]

            nextN = tuple(bestPoint)

            self.data[nextN[0], nextN[1]] = 4
            neigh = self.getNeighbours(nextN, self.data)
            self.trajectory.append(nextN)

    def bfs(self):
        # Mark all the vertices as not visited
        visited = self.data.copy()
        s = self.trajectory[-1]
        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s[0], s[1]] = -2

        parents = dict()
        parents[tuple(s)] = None

        while queue:

            # Dequeue a vertex from
            s = queue.pop(0)

            if self.data[s[0], s[1]] == 3:
                print("Ran this shit")
                path = []
                s = tuple(s)
                while s != None:

                    path.append(s)
                    s = parents[s]

                path.reverse()

                return path

            # Get all adjacent vertices of the
            n = self.getNeighbours(s, visited)
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in n:
                if (i[1] != -2 and i[1] != -1):
                    queue.append(i[0])
                    parents[tuple(i[0])] = tuple(s)
                    visited[i[0][0], i[0][1]] = -2

        return []

    def getTrajectory(self):
        while True:
            self.getWeldLine()
            path = self.bfs()
            if path == []:
                break
            self.trajectory = self.trajectory + path

        for i, t in enumerate(self.trajectory):
            self.data[t[0], t[1]] = 5 + i
