class Node:
    def __init__(self):
        self.parent = 0
        self.size = 0


class Edge:
    def __init__(self, src, dst, wt):
        self.src = src
        self.dst = dst
        self.wt = wt


dsu = []
mst = []


def find(v):
    if dsu[v].parent == v:
        return v
    dsu[v].parent = find(dsu[v].parent)
    return dsu[v].parent


def union(from_, to):
    if dsu[from_].size > dsu[to].size:
        dsu[to].parent = from_
        dsu[from_].size += dsu[to].size
    else:
        dsu[from_].parent = to
        dsu[to].size += dsu[from_].size


def compare_edges(edge):
    return edge.wt


def kruskals(edge_list, v, e):
    edge_list.sort(key=compare_edges)
    i = 0
    j = 0
    while i < v - 1 and j < e:
        from_ = find(edge_list[j].src)
        to = find(edge_list[j].dst)
        if from_ == to:
            j += 1
        else:
            union(from_, to)
            mst.append(edge_list[j])
            i += 1
            j += 1


v, e = map(int, input().split())
edge_list = []
dsu = [Node() for _ in range(v)]

for i in range(v):
    dsu[i].parent = i
    dsu[i].size = 1

for _ in range(e):
    src, dst, wt = map(int, input().split())
    # edge_list.append(Edge(src, dst, wt))
    edge_list.append(Edge(src, dst, wt))

kruskals(edge_list, v, e)

# Print the Minimum Spanning Tree (MST)
for edge in mst:
    print(edge.src, "--", edge.dst, ":", edge.wt)
