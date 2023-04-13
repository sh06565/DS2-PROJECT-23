# ======================== Dijkstra’s Algorithm=====================

# === Dummy Data ===
G = {'A': [('B', 7), ('E', 6), ('D', 2)],
     'B': [('A', 7), ('C', 3)],
     'C': [('B', 3), ('D', 2), ('G', 2)],
     'D': [('A', 2), ('C', 2), ('F', 8)],
     'E': [('A', 6), ('F', 9)],
     'F': [('D', 8), ('E', 9), ('G', 4)],
     'G': [('C', 2), ('F', 4)]}
# === --------- ====

def basic_dijsktra(graph,start,end):
    lst_nodes=list(graph.keys())
    short_dist,visited,infinity={},[],9999
    for each_node in lst_nodes:
        if each_node==start:
            short_dist[each_node]=("", 0)
        else:
            short_dist[each_node]=("", infinity)                
    while len(visited)!=len(lst_nodes):
        lst=[]
        for value in short_dist.items(): 
            if value[0] not in visited:
                lst.append(value[1][1])
        min_d=min(lst)
        for key, value in short_dist.items():
            if min_d==value[1] and key not in visited:
                visited.append(key)
                for val in G[key]:
                    temp=short_dist[key][1] + (val[1])
                    if temp<short_dist[val[0]][1]:
                        short_dist[val[0]]=(key,temp)
    path=[]
    x=""
    y=end
    while x!=start:
        x=short_dist[y][0]
        path.insert(0,(x, y))
        y=x
    print("==>The shortest path is : "+"\n",path)
    # print("The paths are as follows: "+"\n")
    # return short_dist
print("========================Exercise # 2 Part a========================")
basic_dijsktra(G,"A","F")