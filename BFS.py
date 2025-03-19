class Queue:
    def __init__(self):
        self.l=[]

    def enqueue(self,str):
        self.l.append(str)
    def dequeue(self):
        if self.l:
            t=self.l[0]
            del(self.l[0])
            return t
        else:
            return None

def BFS(dict, start_node, destination):
    queue = Queue()
    queue.enqueue(start_node)
    visited = set()
    found=False
    track=[]

    while queue.l and found==False:     #loop untill queue is empty and not reached the destination
        current_node = queue.dequeue()
        if current_node==destination:  #check if we got the destination
            track.append(current_node)
            visited.add(current_node)
            found=True
        else:
            if current_node not in dict.keys(): #check if the current is terminal node
                if current_node not in visited:
                    track.append(current_node)
                    visited.add(current_node)
            else:
                if current_node not in visited:
                    track.append(current_node)
                    visited.add(current_node)
                for i in dict[current_node]:  #enqueue the neighbor nodes of the current node in queue
                    if i not in visited:
                        queue.enqueue(i)

    if found==False:
        print("Node not found")
    else:
        print("Node found")

    print("Traversed path:",track)

def load_graph_from_file(filename):
    graph = {}

    # Open the specified file for reading with 'utf-8-sig' encoding
    with open(filename, 'r',encoding="utf-8-sig") as file:
        # Read each line in the file
        for line in file:
            # Split the line into node and neighbors
            parts = list(map(int, line.strip().split()))  # Convert strings to integers

            # First part is the node, the rest are its neighbors
            node = parts[0]
            neighbors = parts[1:]

            # Add to graph dictionary
            graph[node] = neighbors

    return graph
filename = 'graph.txt'
graph = load_graph_from_file(filename)

BFS(graph, 1,4)
