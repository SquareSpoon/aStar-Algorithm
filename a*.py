from heapq import *
from math import inf
n, m = [int(p) for p in input().split()]
maps = []
start = []
end = []
movesX = [1, 0, -1, 0]
movesY = [0, 1, 0, -1]
#find the start and end positions
def target(l, x):
    global start, end
    for i in range(len(l)):
        if l[i] == 's':
            start.append([x, i])
        elif l[i] == 'e':
            end.append([x, i])
#input the map
for i in range(n):
    w = [p1 for p1 in input().split()]
    target(w, i)
    maps.append(w)
dist = [[] for _ in range(len(maps))]
def set_dist():
    for i in range(n):
        for j in range(m):
            dist[i].append(inf)

#calculate the distance from the start position to current position
def distance(x, y):
    costX = abs(x - start[0][0])
    costY = abs(y - start[0][1])
    total_cost = costX + costY
    return total_cost
#calculate the distance form the current position to the end position
def heuristic(x, y):
    costX = abs(x - end[0][0])
    costY = abs(y - end[0][1])
    total_cost = costX + costY
    return total_cost
#do a bfs using a heap queue instead of a regular queue
def search():
    est_path = {}
    visited = []
    #heap queue 
    v = [(distance(start[0][0], start[0][1])+heuristic(start[0][0], start[0][1]), [start[0][0], start[0][1]])]
    found = False
    idx = 0
    idy = 0
    est_path[0] = [[start[0][0], start[0][1]], 0, []]
    while v:
        l = []
        #take the smallest position in the queue
        prev_dist, step = heappop(v)
        visited.append(step)
        idx += 1
        est_path[idx] = [step, idx-1, []]
        #return the path if you find the end position
        if maps[step[0]][step[1]] == 'e':
            path = []
            f = False
            i = idx-1
            num = est_path[i+1][0]
            while f == False:
                if num in est_path[i][2]:
                    num = est_path[i][0]
                    if est_path[i][1] == 0:
                        f = True
                    path.append(num) 
                i -= 1
            return path
        #move in the map
        for i in range(4):
            x = step[0] + movesX[i]
            y = step[1] + movesY[i]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if maps[x][y] == '#' or [x, y] in visited:
                continue
            #calculate the distances and add the point to the queue
            if [x, y] not in visited:
                d = distance(x, y) + heuristic(x, y)
                if d < dist[x][y] and (d, [x, y]) not in v:
                    dist[x][y] = d
                    l.append([x, y])
                    heappush(v, (d, [x, y]))
        est_path[idx][2] = l
    return 'path not found'
set_dist()
p = search()
#print the path
print()
for i in range(n):
    for j in range(m):
        if [i, j] in p or maps[i][j] == 'e':
            print('*', end=" ")
        else:
            print(maps[i][j], end=" ")
    print()