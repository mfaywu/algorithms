'''
Implement DFS and BFS
hasPath(start, end) -> true or False
getPaths(start, end) -> return all paths from start to end
getShortestPath(start, end) -> return shortest path from start to end

'''

class Graph():
    graph = {}

    def __init__(self, graph):
        self.graph = graph

    def hasPathDFS(self, start, end):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex == end:
                return True
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.graph[vertex] - visited)
        return False

    def hasPathBFS(self, start, end):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex == end:
                return True
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph[vertex] - visited)
        return False

    def getPathsDFS(self, start, end):
        if start == end:
            yield [start]
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in self.graph[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def getPathsBFS(self, start, end):
        if start == end:
            yield [start]
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.graph[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def getShortestPathDFS(self, start, end):
        try:
            return next(self.getPathsDFS( start, end))
        except StopIteration:
            return None

    def getShortestPathBFS(self, start, end):
        try:
            return next(self.getPathsBFS( start, end))
        except StopIteration:
            return None


people = {
    'Jackie': set(['Jon', 'Carl', 'Abe']), 
    'Jon': set(['Jackie', 'Chris']), 
    'Carl': set(['Jackie', 'Chris']), 
    'Abe': set(['Jackie']), 
    'Chris': set(['Jon', 'Carl']), 
    'Jake': set(['Abby']), 
    'Abby': set(['Jake'])
}

graph = Graph(people)
print graph.hasPathDFS('Jackie', 'Carl') == True
print graph.hasPathBFS('Jackie', 'Carl') == True

print list(graph.getPathsDFS('Jackie', 'Chris'))
print list(graph.getPathsDFS('Jackie', 'Jackie'))
print list(graph.getPathsDFS('Jackie', 'Abby'))

print list(graph.getPathsBFS('Jackie', 'Chris'))
print list(graph.getPathsBFS('Jackie', 'Jackie'))
print list(graph.getPathsBFS('Jackie', 'Abby'))

print graph.getShortestPathDFS('Jackie', 'Abby')
print graph.getShortestPathDFS('Jackie', 'Chris')