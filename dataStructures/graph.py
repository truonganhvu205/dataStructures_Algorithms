class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}

        for start, end in edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            self.graphDict[start] = [end]

        print('Graph Dict:', self.graphDict)

    def getFullPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graphDict:
            return []
        
        fullPath = []

        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getFullPath(node, end, path)

                for fp in newPath:
                    fullPath.append(fp)

        return fullPath
    
    def getShortestPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graphDict:
            return None
        
        shortestPath = None

        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getShortestPath(node, end, path)

                if newPath:
                    if shortestPath is None or len(shortestPath) > len(newPath):
                        shortestPath = newPath

        return shortestPath
    
if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]

    routesGraph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'

    print(f'Full path between {start} and {end}:', routesGraph.getFullPath(start, end))
    print(f'Shortest path between {start} and {end}:', routesGraph.getShortestPath(start, end))