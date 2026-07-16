// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

import (
	"container/heap"
)

type mazeState struct {
	dist int
	row  int
	col  int
}

type mazeHeap []mazeState

func (states mazeHeap) Len() int            { return len(states) }
func (states mazeHeap) Less(i, j int) bool  { return states[i].dist < states[j].dist }
func (states mazeHeap) Swap(i, j int)       { states[i], states[j] = states[j], states[i] }
func (states *mazeHeap) Push(value interface{}) {
	*states = append(*states, value.(mazeState))
}
func (states *mazeHeap) Pop() interface{} {
	old := *states
	item := old[len(old)-1]
	*states = old[:len(old)-1]
	return item
}

func shortestDistance(maze [][]int, start []int, destination []int) int {
	rows := len(maze)
	cols := len(maze[0])
	targetRow, targetCol := destination[0], destination[1]
	directions := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	best := make([][]int, rows)
	for row := range best {
		best[row] = make([]int, cols)
		for col := range best[row] {
			best[row][col] = 1 << 30
		}
	}

	priority := &mazeHeap{}
	heap.Init(priority)
	heap.Push(priority, mazeState{dist: 0, row: start[0], col: start[1]})

	for priority.Len() > 0 {
		current := heap.Pop(priority).(mazeState)
		if current.row == targetRow && current.col == targetCol {
			return current.dist
		}
		if best[current.row][current.col] <= current.dist {
			continue
		}
		best[current.row][current.col] = current.dist

		for _, direction := range directions {
			nextRow, nextCol := current.row, current.col
			traveled := 0
			for nextRow+direction[0] >= 0 && nextRow+direction[0] < rows &&
				nextCol+direction[1] >= 0 && nextCol+direction[1] < cols &&
				maze[nextRow+direction[0]][nextCol+direction[1]] == 0 {
				nextRow += direction[0]
				nextCol += direction[1]
				traveled++
			}
			if nextRow == current.row && nextCol == current.col {
				continue
			}
			newDist := current.dist + traveled
			if newDist < best[nextRow][nextCol] {
				heap.Push(priority, mazeState{dist: newDist, row: nextRow, col: nextCol})
			}
		}
	}
	return -1
}
