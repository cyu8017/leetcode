// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/


import "container/heap"

type item struct{ t, r, c int }
type pq []item
func (h pq) Len() int            { return len(h) }
func (h pq) Less(i, j int) bool  { return h[i].t < h[j].t }
func (h pq) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pq) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *pq) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumTime(grid [][]int) int {
	if grid[0][1] > 1 && grid[1][0] > 1 {
		return -1
	}
	m, n := len(grid), len(grid[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	h := &pq{{0, 0, 0}}
	heap.Init(h)
	dist[0][0] = 0
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.r == m-1 && cur.c == n-1 {
			return cur.t
		}
		if cur.t > dist[cur.r][cur.c] {
			continue
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}
			nt := cur.t + 1
			if nt < grid[nr][nc] {
				wait := grid[nr][nc] - nt
				if wait%2 == 1 {
					wait++
				}
				nt += wait
			}
			if nt < dist[nr][nc] {
				dist[nr][nc] = nt
				heap.Push(h, item{nt, nr, nc})
			}
		}
	}
	return -1
}
