// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

import "container/heap"

type node3342 struct{ t, r, c, parity int }
type h3342 []node3342

func (h h3342) Len() int            { return len(h) }
func (h h3342) Less(i, j int) bool  { return h[i].t < h[j].t }
func (h h3342) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *h3342) Push(x interface{}) { *h = append(*h, x.(node3342)) }
func (h *h3342) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minTimeToReach(moveTime [][]int) int {
	m, n := len(moveTime), len(moveTime[0])
	dist := make([][][2]int, m)
	for i := range dist {
		dist[i] = make([][2]int, n)
		for j := range dist[i] {
			dist[i][j] = [2]int{1 << 30, 1 << 30}
		}
	}
	h := &h3342{{0, 0, 0, 0}}
	dist[0][0][0] = 0
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(node3342)
		if cur.t != dist[cur.r][cur.c][cur.parity] {
			continue
		}
		if cur.r == m-1 && cur.c == n-1 {
			return cur.t
		}
		cost := 1
		if cur.parity == 1 {
			cost = 2
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
			nt := start + cost
			np := 1 - cur.parity
			if nt < dist[nr][nc][np] {
				dist[nr][nc][np] = nt
				heap.Push(h, node3342{nt, nr, nc, np})
			}
		}
	}
	return -1
}
