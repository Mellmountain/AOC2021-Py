from queue import PriorityQueue
input = list(open('Day15\\input.txt').read().splitlines())

G = []
for line in input:
    G.append([int(x) for x in line.strip()])

DR = [-1, 0, 1,  0]
DC = [ 0, 1, 0, -1]

R = len(G)
C = len(G[0])

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = PriorityQueue()
    Q.put((0, 0, 0))

    while Q:
        (dist, r, c) = Q.get()
        if r < 0 or r >= n_tiles*R or c < 0 or c >= n_tiles*C:
            continue
        
        val = G[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        if D[r][c] is None or dist + val < D[r][c]:
            D[r][c] = dist + val
        else:
            continue
        
        if r == n_tiles*R - 1 and c == n_tiles*C - 1:
            break

        for i in range(4):
            rr = r + DR[i]
            cc = c + DC[i]
            Q.put((D[r][c], rr, cc))
    return D[n_tiles*R-1][n_tiles*C-1] - G[0][0]

print("Part 1: ", solve(1))
print("Part 2: ", solve(5))



    
        
