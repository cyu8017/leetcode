// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

import "container/heap"
import "sort"

type cell struct{ r, c, v int }
type minHeap []cell

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].v < h[j].v }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(cell)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxPoints(grid [][]int, queries []int) []int {
	m, n := len(grid), len(grid[0])
	order := make([]int, len(queries))
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool { return queries[order[i]] < queries[order[j]] })
	ans := make([]int, len(queries))
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	h := &minHeap{{0, 0, grid[0][0]}}
	heap.Init(h)
	visited[0][0] = true
	points := 0
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for _, qi := range order {
		q := queries[qi]
		for h.Len() > 0 && (*h)[0].v < q {
			cur := heap.Pop(h).(cell)
			points++
			for _, d := range dirs {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] {
					visited[nr][nc] = true
					heap.Push(h, cell{nr, nc, grid[nr][nc]})
				}
			}
		}
		ans[qi] = points
	}
	return ans
}
