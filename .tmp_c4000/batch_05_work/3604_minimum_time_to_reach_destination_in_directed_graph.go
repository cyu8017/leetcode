// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

import (
	"container/heap"
)

func minTime(n int, edges [][]int) int {
	type edge struct{ to, start, end int }
	g := make([][]edge, n)
	for _, e := range edges {
		u, v, s, en := e[0], e[1], e[2], e[3]
		g[u] = append(g[u], edge{v, s, en})
	}
	const inf = int(1e18)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = inf
	}
	dist[0] = 0
	// Dijkstra
	h := &minHeap{}
	heap.Push(h, item{0, 0})
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.t != dist[cur.u] {
			continue
		}
		if cur.u == n-1 {
			return cur.t
		}
		for _, e := range g[cur.u] {
			t := cur.t
			if t > e.end {
				continue
			}
			if t < e.start {
				t = e.start
			}
			nt := t + 1
			if nt < dist[e.to] {
				dist[e.to] = nt
				heap.Push(h, item{e.to, nt})
			}
		}
	}
	if dist[n-1] == inf {
		return -1
	}
	return dist[n-1]
}

type item struct{ u, t int }
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].t < h[j].t }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}
