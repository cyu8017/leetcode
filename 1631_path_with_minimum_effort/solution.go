// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

import "container/heap"

type effortItem struct {
	effort, i, j int
}

type effortHeap []effortItem

func (h effortHeap) Len() int            { return len(h) }
func (h effortHeap) Less(i, j int) bool  { return h[i].effort < h[j].effort }
func (h effortHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *effortHeap) Push(x interface{}) { *h = append(*h, x.(effortItem)) }
func (h *effortHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumEffortPath(heights [][]int) int {
	m, n := len(heights), len(heights[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	dist[0][0] = 0
	h := &effortHeap{{0, 0, 0}}
	heap.Init(h)
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(effortItem)
		if cur.i == m-1 && cur.j == n-1 {
			return cur.effort
		}
		if cur.effort != dist[cur.i][cur.j] {
			continue
		}
		for _, d := range dirs {
			x, y := cur.i+d[0], cur.j+d[1]
			if x >= 0 && x < m && y >= 0 && y < n {
				diff := heights[cur.i][cur.j] - heights[x][y]
				if diff < 0 {
					diff = -diff
				}
				nd := cur.effort
				if diff > nd {
					nd = diff
				}
				if nd < dist[x][y] {
					dist[x][y] = nd
					heap.Push(h, effortItem{nd, x, y})
				}
			}
		}
	}
	return 0
}
