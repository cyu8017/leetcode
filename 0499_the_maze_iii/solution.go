// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

import (
	"container/heap"
)

type mazeState struct {
	dist int
	path string
	row  int
	col  int
}

type mazeHeap []mazeState

func (states mazeHeap) Len() int { return len(states) }
func (states mazeHeap) Less(i, j int) bool {
	if states[i].dist != states[j].dist {
		return states[i].dist < states[j].dist
	}
	return states[i].path < states[j].path
}
func (states mazeHeap) Swap(i, j int) { states[i], states[j] = states[j], states[i] }
func (states *mazeHeap) Push(value interface{}) {
	*states = append(*states, value.(mazeState))
}
func (states *mazeHeap) Pop() interface{} {
	old := *states
	item := old[len(old)-1]
	*states = old[:len(old)-1]
	return item
}

func findShortestWay(maze [][]int, ball []int, hole []int) string {
	rows := len(maze)
	cols := len(maze[0])
	holeRow, holeCol := hole[0], hole[1]
	directions := [4][2]int{{1, 0}, {0, -1}, {0, 1}, {-1, 0}}
	labels := [4]byte{'d', 'l', 'r', 'u'}

	roll := func(row, col, dr, dc int) (int, int, int) {
		distance := 0
		for row+dr >= 0 && row+dr < rows && col+dc >= 0 && col+dc < cols && maze[row+dr][col+dc] == 0 {
			row += dr
			col += dc
			distance++
			if row == holeRow && col == holeCol {
				break
			}
		}
		return row, col, distance
	}

	best := make([]mazeState, rows*cols)
	for index := range best {
		best[index].dist = 1 << 30
	}

	priority := &mazeHeap{}
	heap.Init(priority)
	heap.Push(priority, mazeState{dist: 0, path: "", row: ball[0], col: ball[1]})

	for priority.Len() > 0 {
		current := heap.Pop(priority).(mazeState)
		stateIndex := current.row*cols + current.col
		if best[stateIndex].dist < current.dist ||
			(best[stateIndex].dist == current.dist && best[stateIndex].path <= current.path) {
			continue
		}
		best[stateIndex] = current
		if current.row == holeRow && current.col == holeCol {
			return current.path
		}

		for index := 0; index < 4; index++ {
			nextRow, nextCol, traveled := roll(current.row, current.col, directions[index][0], directions[index][1])
			if nextRow == current.row && nextCol == current.col {
				continue
			}
			newDist := current.dist + traveled
			newPath := current.path + string(labels[index])
			targetIndex := nextRow*cols + nextCol
			if newDist < best[targetIndex].dist ||
				(newDist == best[targetIndex].dist && newPath < best[targetIndex].path) {
				heap.Push(priority, mazeState{dist: newDist, path: newPath, row: nextRow, col: nextCol})
			}
		}
	}
	return "impossible"
}
