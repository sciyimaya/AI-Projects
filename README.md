# 8 or 15 Tile Puzzle Solver

Tile puzzle solver program uses A* and RBFS algorithms to solve the 8 or 15 tile puzzle problem.
## How to Run

```bash
python puzzleSolver.py <A> <N> <H> <INPUT_FILE_PATH> <OUTPUT_FILE_PATH>
```
where A is the algorithm (A=1 for A* and A=2 for RBFS), N is the size of puzzle (N=3 for 8-puzzle and N=4 for 15-puzzle), H is for heuristics (H=1 for h1 and H=2 for h2), INPUT FILE PATH and OUTPUT FILE PATH are the input and output filenames.

Heuristic 1 checks the number of misplaced tiles in the whole board while h2 looks at the number of misplaced tiles excluding the last 4. 

```bash
Exemplary 8-puzzle file:
                              1,2,3 
                              4,5,6 
                              ,7,8

Exemplary 15-puzzle file:
                               1,2,3,4 
                               5,6,7,8 
                               10,11,,12 
                               9,13,14,15
```
## Output

```bash
INPUT:

                               1,3,
                               4,2,5
                               7,8,6

OUTPUT:
                               L,D,R,D
```

L → Move blank tile left, 
R → Move blank tile right 
D → Move blank tile down, 
U → Move blank tile up
