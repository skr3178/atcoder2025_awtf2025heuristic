# Takes in the input file of /Users/skr3178/Downloads/tools/0000.txt

input_file = "/Users/skr3178/Downloads/tools/0000.txt"

with open(input_file, 'r') as file:
    lines = file.readlines()

N = int(lines[0].split()[0])
K = int(lines[0].split()[1])

# ss refers to the start coordinates of the robot(i0, j0)
# ts refers to the end coordinates of the robot(i_k, j_k)
ss = []
ts = []
for i in range(1, K+1):
    ss.append((int(lines[i].split()[0]), int(lines[i].split()[1])))
    ts.append((int(lines[i].split()[2]), int(lines[i].split()[3])))

wall_v = []
wall_h = []

# wall_v refers to the vertical walls
# wall_h refers to the horizontal walls

# get the vertical walls and the horizontal walls
for i in range(1+K, 1+K+N):
    wall_v.append(list(lines[i].strip()))
for i in range(1+K+N, 1+K+2*N-1):
    wall_h.append(list(lines[i].strip()))


# as test case, we can use treat the entire as individual control
# chart a direct path from start to end for each robot

# function to check if the path is valid
def is_valid_path(path, wall_v, wall_h):
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        if x1 == x2:
            if wall_v[x1][y1] == '1':
                return False
        if y1 == y2:
            if wall_h[x1][y1] == '1':
                return False
    return True 

# function to get the next position
def get_next_position(x, y, direction):
    if direction == 'U':
        return x-1, y
    elif direction == 'D':
        return x+1, y
    elif direction == 'L':
        return x, y-1
    elif direction == 'R':
        return x, y+1

paths = []

for i in range(K):
    path = [(sx, sy)]
    sx, sy = ss[i]
    tx, ty = ts[i]
    while sx != tx or sy != ty: # direct path from start to end
        path.append((sx, sy))
        if sx < tx:
            sx += 1
        elif sx > tx:
            sx -= 1

        if sy < ty:
            sy += 1
        elif sy > ty:
            sy -= 1
    paths.append(path)

# Calculate the total number of operations
total_operations = 0
for i in range(K):
    sx, sy = ss[i]
    tx, ty = ts[i]
    total_operations += abs(sx - tx) + abs(sy - ty)

# Calculate the total distance between start and end
total_distance = 0
for i in range(K):
    sx, sy = ss[i]
    tx, ty = ts[i]
    total_distance += abs(sx - tx) + abs(sy - ty)

# Calculate the reward
reward = total_operations + 100 * total_distance


# a_i : individual
# b_i : robot index
# d_i : turn value

# for example, if the robot is at (0, 0), and the turn value is L, then the robot will move to (0, -1)
# if the robot is at (0, 0), and the turn value is R, then the robot will move to (0, 1)
# if the robot is at (0, 0), and the turn value is T, then the robot will move to (-1, 0)
# if the robot is at (0, 0), and the turn value is B, then the robot will move to (1, 0)


# The input file has the following format:
#
# first line : N (number of rows and columns) K (number of robots)
# next K lines : i0, j0 (start coordinates of the robot) i_k, j_k (end coordinates of the robot)
# next N lines : v_i (vertical walls) : 0 or 1
# next N-1 lines : h_i (horizontal walls) : 0 or 1

# reward is given as T (total number of operations) + 100 * (manhattan distance between start to end)

# Output the file information
# First N lines : v_i (vertical walls) : 0 or 1
# Next N lines : h_i (horizontal walls) : 0 or 1

# next K lines : g_i (group index for the robot)

# next K lines : a_i, b_i, d_i (individual or group, turn value)
# a_i : individual or group
# b_i : robot index
# d_i : turn value


