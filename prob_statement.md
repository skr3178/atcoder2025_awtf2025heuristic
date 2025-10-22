# A - Group Commands and Wall Planning

**Time Limit:** 2 sec / **Memory Limit:** 1024 MiB

## Problem Statement

There is an N×N grid. The coordinate of the top-left cell is (0,0), and the coordinate of the cell i rows down and j columns to the right is (i,j). There are walls between some adjacent cells.

There are K robots on the grid. The initial position of the k-th robot is (i_k, j_k), and its destination is (i_k', j_k'). Takahashi wants to operate these robots to bring all of them to their respective destinations.

First, the following two types of preparations can be made:

1. In addition to the existing walls, you may add walls between any adjacent cells.
2. Divide the robots into groups. Each robot belongs to exactly one group, and all robots in the same group can be operated simultaneously.

These preparations must be completed before the first move. After that, no additional walls can be placed and the group assignments cannot be changed.

Next, the robots can be moved by repeatedly performing the following two types of operations:

1. **Group Command**: Specify a group and a direction (up, down, left, or right). All robots in that group will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move. Among the robots belonging to the group, those farthest in the direction of movement will attempt to move first. For example, if robots are at (1,0) and (2,0) and the direction is up, the robot at (1,0) will move to (0,0) first (since it has a smaller i coordinate), and then the robot at (2,0) will move to the now-empty (1,0).

2. **Individual Command**: Specify a robot and a direction (up, down, left, or right). The specified robot will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move.

Even if a robot reaches its destination once, if it moves away from the destination due to subsequent operations, it is not considered to have reached its destination.

You may perform at most KN² operations. Guide all robots to their destinations using as few operations as possible.

## Scoring

Let T be the number of operations performed, and let d_k be the Manhattan distance between the final position and the destination of robot k. Then, you obtain the following absolute score:

**T + 100 × Σ_k d_k**

The lower the absolute score, the better.

For each test case, we compute the relative score round(10^9 × MIN/YOUR), where YOUR is your absolute score and MIN is the lowest absolute score among all competitors obtained on that test case. The score of the submission is the sum of the relative scores.

The final ranking will be determined by the system test with more inputs which will be run after the contest is over. In both the provisional/system test, if your submission produces illegal output or exceeds the time limit for some test cases, only the score for those test cases will be zero, and your submission will be excluded from the MIN calculation for those test cases.

The system test will be performed only for the last submission which received a result other than CE. Be careful not to make a mistake in the final submission.

### Number of test cases
- Provisional test: 50
- System test: 2000. We will publish seeds.txt (sha256=063a84b1c0dc9388b0996eed0bc645529c931c139bee6b8e0e84a4faf3e06c40) after the contest is over.

### About relative evaluation system
In both the provisional/system test, the standings will be calculated using only the last submission which received a result other than CE. Only the last submissions are used to calculate the MIN for each test case when calculating the relative scores.

The scores shown in the standings are relative, and whenever a new submission arrives, all relative scores are recalculated. On the other hand, the score for each submission shown on the submissions page is the sum of the absolute score for each test case, and the relative scores are not shown. In order to know the relative score of submission other than the latest one in the current standings, you need to resubmit it. If your submission produces illegal output or exceeds the time limit for some test cases, the score shown on the submissions page will be 0, but the standings show the sum of the relative scores for the test cases that were answered correctly.

### About execution time
Execution time may vary slightly from run to run. In addition, since system tests simultaneously perform a large number of executions, it has been observed that execution time increases by several percent compared to provisional tests. For these reasons, submissions that are very close to the time limit may result in TLE in the system test. Please measure the execution time in your program to terminate the process, or have enough margin in the execution time.

## Input

Input is given from Standard Input in the following format:

```
N K
i_0 j_0 i_0' j_0'
⋮
i_{K-1} j_{K-1} i_{K-1}' j_{K-1}'
v_{0,0} ⋯ v_{0,N-2}
⋮
v_{N-1,0} ⋯ v_{N-1,N-2}
h_{0,0} ⋯ h_{0,N-1}
⋮
h_{N-2,0} ⋯ h_{N-2,N-1}
```

- In all test cases, N=30 is fixed.
- 10≤K≤100
- (i_k, j_k) represents the initial position of the k-th robot.
- (i_k', j_k') represents the destination of the k-th robot.
- All initial positions and all destinations are each mutually distinct, but the initial position of robot k may coincide with the destination of robot k'.
- Each v_{i,0} ⋯ v_{i,N-2} is a binary string of length N-1. The j-th character v_{i,j} indicates whether there is a wall (1) or not (0) between cells (i,j) and (i,j+1).
- Each h_{i,0} ⋯ h_{i,N-1} is a binary string of length N. The j-th character h_{i,j} indicates whether there is a wall (1) or not (0) between cells (i,j) and (i+1,j).
- It is guaranteed that all cells are mutually reachable.
## Output

First, output the wall placement information in the following format to Standard Output:

```
v'_{0,0} ⋯ v'_{0,N-2}
⋮
v'_{N-1,0} ⋯ v'_{N-1,N-2}
h'_{0,0} ⋯ h'_{0,N-1}
⋮
h'_{N-2,0} ⋯ h'_{N-2,N-1}
```

- Each v'_{i,0} ⋯ v'_{i,N-2} is a binary string of length N-1. The j-th character v'_{i,j} indicates whether a wall is placed (1) or not (0) between cells (i,j) and (i,j+1).
- Each h'_{i,0} ⋯ h'_{i,N-1} is a binary string of length N. The j-th character h'_{i,j} indicates whether a wall is placed (1) or not (0) between cells (i,j) and (i+1,j).
- For positions where a wall already exists, either 0 or 1 may be output.

Next, output the group assignment information to Standard Output in the following format:

```
g_0 ⋯ g_{K-1}
```

- g_k is an integer between 0 and K-1 representing the group to which the k-th robot belongs. If g_k = g_{k'}, then robot k and robot k' belong to the same group.

Finally, output the sequence of operations to Standard Output in the following format:

```
a_0 b_0 d_0
⋮
a_{T-1} b_{T-1} d_{T-1}
```

- a_t is a single character specifying the type of operation on turn t. Use g for a group command and i for an individual command.
- b_t is an integer between 0 and K-1 representing the group number or robot number targeted by the operation on turn t. If a group with no robots is specified, nothing happens.
- d_t is a single character indicating the direction of the operation on turn t, as follows:
  - Up: U
  - Down: D
  - Left: L
  - Right: R