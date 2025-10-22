import sys
from collections import deque, defaultdict
import heapq

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    K = int(input[ptr])
    ptr += 1

    robots = []
    for _ in range(K):
        i, j, di, dj = map(int, input[ptr:ptr+4])
        ptr += 4
        robots.append(((i, j), (di, dj)))

    v_walls = []
    for _ in range(N):
        row = input[ptr]
        ptr += 1
        v_walls.append(row)

    h_walls = []
    for _ in range(N-1):
        row = input[ptr]
        ptr += 1
        h_walls.append(row)

    # Output walls (no additional walls for simplicity)
    for row in v_walls:
        print(row)
    for row in h_walls:
        print(row)

    # Assign groups based on destination regions
    groups = []
    for idx, ((i, j), (di, dj)) in enumerate(robots):
        region = (di // 10) * 3 + (dj // 10)
        groups.append(region)
    print(' '.join(map(str, groups)))

    # A* to find path for each robot
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    reverse_dir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    operations = []
    occupied = defaultdict(bool)
    for idx, ((i, j), (di, dj)) in enumerate(robots):
        occupied[(i, j)] = True

    for idx, ((i, j), (di, dj)) in enumerate(robots):
        # A* to find path from (i,j) to (di,dj)
        def heuristic(x, y):
            return abs(x - di) + abs(y - dj)

        heap = []
        heapq.heappush(heap, (heuristic(i, j), i, j))
        visited = {}
        visited[(i, j)] = (0, None, None)
        found = False
        while heap:
            _, x, y = heapq.heappop(heap)
            if x == di and y == dj:
                found = True
                break
            for dir, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    # Check wall
                    if dir == 'U' and h_walls[x-1][y] == '1':
                        continue
                    if dir == 'D' and h_walls[x][y] == '1':
                        continue
                    if dir == 'L' and v_walls[x][y-1] == '1':
                        continue
                    if dir == 'R' and v_walls[x][y] == '1':
                        continue
                    new_cost = visited[(x, y)][0] + 1
                    if (nx, ny) not in visited or new_cost < visited[(nx, ny)][0]:
                        visited[(nx, ny)] = (new_cost, (x, y), dir)
                        heapq.heappush(heap, (new_cost + heuristic(nx, ny), nx, ny))
        if not found:
            pass
        # Reconstruct path
        path = []
        x, y = di, dj
        while (x, y) != (i, j):
            _, (x_prev, y_prev), dir = visited[(x, y)]
            path.append(reverse_dir[dir])
            x, y = x_prev, y_prev
        path.reverse()
        # Generate operations
        for move in path:
            operations.append(f"i {idx} {move}")

    # Output operations
    for op in operations:
        print(op)

if __name__ == "__main__":
    main()