# How We Solve Pacific Atlantic Water Flow

DFS from both oceans and intersect reachable cells.

## Steps

1. Flood from Pacific borders and Atlantic borders separately.
2. Only move to equal or higher heights.
3. Return coordinates reachable from both oceans.
