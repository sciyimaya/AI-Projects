# Constraint Satisfaction

Constraint Satisfaction is a python program that solves constraint satisfaction problems. These problems has number of variables (N), number of edges in between variables (M), number of possible variables in the domain (K), and assignment data structure where we keep the current state of problem.

## Algorihms Used
- Plain DFS-B and b) DFS-B with variable, value ordering + AC3 for constraint propagation.
- MinConflicts local search algorithm.

## Installation

min python version 3.7

## How to Run
```bash
python dfsb.py <INPUT FILE> <OUTPUT FILE> <MODE FLAG>
```
- <INPUT FILE> is the url of the file that contains csp problem description.
- <OUTPUT FILE> is the url of the file that will contains solution or possible no solution for the csp problem.
- <MODE FLAG> can be either 0 (plain DFS-B) or 1 (improved DFS-B).

```bash
python minconflicts.py <INPUT FILE> <OUTPUT FILE>
```

The sample input and the outpt file formats shown below.

Input:		
3   2   2       
0 2			
1 2			

Output:
0 
0
1 
## Performance Comparison 
```bash
python CSPGenerator.py <N> <M> <K> <output file path> 
```
where <N>, <M>, <K> are the same as above. output file path is output file path for test problem. This script can not guarantee to generate test problem for given parameters. The generated csp are exclusive, so the script would fail if M is too large.

```bash
python CSPGenerator.py <N> <M> <K> <output file path> 0
```
To generate random problem (which may not be solvable and we will not evaluate on)


