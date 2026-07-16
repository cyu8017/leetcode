// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

import (
	"container/heap"
)

type cellEntry struct {
	height int
	row    int
	col    int
}

type cellHeap []cellEntry

func (h cellHeap) Len() int            { return len(h) }
func (h cellHeap) Less(i, j int) bool  { return h[i].height < h[j].height }
func (h cellHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *cellHeap) Push(x interface{}) { *h = append(*h, x.(cellEntry)) }
func (h *cellHeap) Pop() interface{} {
	items := *h
	item := items[len(items)-1]
	*h = items[:len(items)-1]
	return item
}

func trapRainWater(heightMap [][]int) int {
	if len(heightMap) == 0 || len(heightMap[0]) == 0 {
		return 0
	}

	rows := len(heightMap)
	cols := len(heightMap[0])
	if rows < 3 || cols < 3 {
		return 0
	}

	visited := make([][]bool, rows)
	for row := 0; row < rows; row++ {
		visited[row] = make([]bool, cols)
	}

	minHeap := make(cellHeap, 0)
	heap.Init(&minHeap)

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if row == 0 || row == rows-1 || col == 0 || col == cols-1 {
				heap.Push(&minHeap, cellEntry{height: heightMap[row][col], row: row, col: col})
				visited[row][col] = true
			}
		}
	}

	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	trapped := 0

	for len(minHeap) > 0 {
		top := heap.Pop(&minHeap).(cellEntry)
		for _, direction := range directions {
			nextRow := top.row + direction[0]
			nextCol := top.col + direction[1]
			if nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol] {
				continue
			}

			visited[nextRow][nextCol] = true
			nextHeight := heightMap[nextRow][nextCol]
			if top.height > nextHeight {
				trapped += top.height - nextHeight
			}
			borderHeight := top.height
			if nextHeight > borderHeight {
				borderHeight = nextHeight
			}
			heap.Push(&minHeap, cellEntry{height: borderHeight, row: nextRow, col: nextCol})
		}
	}

	return trapped
}
