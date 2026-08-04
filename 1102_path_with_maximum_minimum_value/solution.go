// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

import "container/heap"

type maxPathItem struct {
	val, r, c int
}

type maxPathHeap []maxPathItem

func (h maxPathHeap) Len() int            { return len(h) }
func (h maxPathHeap) Less(i, j int) bool  { return h[i].val > h[j].val }
func (h maxPathHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxPathHeap) Push(x interface{}) { *h = append(*h, x.(maxPathItem)) }
func (h *maxPathHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maximumMinimumPath(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	h := &maxPathHeap{{grid[0][0], 0, 0}}
	heap.Init(h)
	seen := make([][]bool, m)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	seen[0][0] = true
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(maxPathItem)
		if cur.r == m-1 && cur.c == n-1 {
			return cur.val
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc] {
				seen[nr][nc] = true
				v := cur.val
				if grid[nr][nc] < v {
					v = grid[nr][nc]
				}
				heap.Push(h, maxPathItem{v, nr, nc})
			}
		}
	}
	return grid[0][0]
}
