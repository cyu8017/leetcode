// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

import "container/heap"

type cell struct {
	time, r, c int
}
type cellHeap []cell

func (h cellHeap) Len() int            { return len(h) }
func (h cellHeap) Less(i, j int) bool  { return h[i].time < h[j].time }
func (h cellHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *cellHeap) Push(x interface{}) { *h = append(*h, x.(cell)) }
func (h *cellHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func swimInWater(grid [][]int) int {
	n := len(grid)
	h := &cellHeap{{grid[0][0], 0, 0}}
	heap.Init(h)
	seen := map[[2]int]bool{{0, 0}: true}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(cell)
		if cur.r == n-1 && cur.c == n-1 {
			return cur.time
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[[2]int{nr, nc}] {
				seen[[2]int{nr, nc}] = true
				t := cur.time
				if grid[nr][nc] > t {
					t = grid[nr][nc]
				}
				heap.Push(h, cell{t, nr, nc})
			}
		}
	}
	return -1
}
