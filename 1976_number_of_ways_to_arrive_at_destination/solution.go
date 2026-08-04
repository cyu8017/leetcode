// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

import "container/heap"

type pathItem struct {
	dist, node int64
}

type pathHeap []pathItem

func (h pathHeap) Len() int            { return len(h) }
func (h pathHeap) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h pathHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pathHeap) Push(x interface{}) { *h = append(*h, x.(pathItem)) }
func (h *pathHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func countPaths(n int, roads [][]int) int {
	const MOD = 1000000007
	g := make([][][2]int, n)
	for _, r := range roads {
		u, v, t := r[0], r[1], r[2]
		g[u] = append(g[u], [2]int{v, t})
		g[v] = append(g[v], [2]int{u, t})
	}
	dist := make([]int64, n)
	ways := make([]int, n)
	for i := range dist {
		dist[i] = 1 << 62
	}
	dist[0] = 0
	ways[0] = 1
	h := &pathHeap{{0, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(pathItem)
		if cur.dist > dist[cur.node] {
			continue
		}
		u := int(cur.node)
		for _, e := range g[u] {
			v, w := e[0], int64(e[1])
			nd := cur.dist + w
			if nd < dist[v] {
				dist[v] = nd
				ways[v] = ways[u]
				heap.Push(h, pathItem{nd, int64(v)})
			} else if nd == dist[v] {
				ways[v] = (ways[v] + ways[u]) % MOD
			}
		}
	}
	return ways[n-1]
}
