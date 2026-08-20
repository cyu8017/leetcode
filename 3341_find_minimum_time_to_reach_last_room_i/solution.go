// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

import "container/heap"

type node3341 struct{ t, r, c int }
type h3341 []node3341

func (h h3341) Len() int            { return len(h) }
func (h h3341) Less(i, j int) bool  { return h[i].t < h[j].t }
func (h h3341) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *h3341) Push(x interface{}) { *h = append(*h, x.(node3341)) }
func (h *h3341) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minTimeToReach(moveTime [][]int) int {
	m, n := len(moveTime), len(moveTime[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	h := &h3341{{0, 0, 0}}
	dist[0][0] = 0
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(node3341)
		if cur.t != dist[cur.r][cur.c] {
			continue
		}
		if cur.r == m-1 && cur.c == n-1 {
			return cur.t
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nc < 0 || nr >= m || nc >= n {
				continue
			}
			start := cur.t
			if moveTime[nr][nc] > start {
				start = moveTime[nr][nc]
			}
			nt := start + 1
			if nt < dist[nr][nc] {
				dist[nr][nc] = nt
				heap.Push(h, node3341{nt, nr, nc})
			}
		}
	}
	return -1
}
