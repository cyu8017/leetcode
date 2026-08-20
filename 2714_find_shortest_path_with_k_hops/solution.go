// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/


import "container/heap"

type st struct{ node, hops, dist int }
type sth []st
func (h sth) Len() int            { return len(h) }
func (h sth) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h sth) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *sth) Push(x interface{}) { *h = append(*h, x.(st)) }
func (h *sth) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func shortestPathWithHops(n int, edges [][]int, s int, d int, k int) int {
	g := make([][][2]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], [2]int{v, w})
		g[v] = append(g[v], [2]int{u, w})
	}
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, k+1)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	dist[s][0] = 0
	h := &sth{{s, 0, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(st)
		if cur.node == d {
			return cur.dist
		}
		if cur.dist > dist[cur.node][cur.hops] {
			continue
		}
		for _, e := range g[cur.node] {
			to, w := e[0], e[1]
			if nd := cur.dist + w; nd < dist[to][cur.hops] {
				dist[to][cur.hops] = nd
				heap.Push(h, st{to, cur.hops, nd})
			}
			if cur.hops < k {
				if nd := cur.dist; nd < dist[to][cur.hops+1] {
					dist[to][cur.hops+1] = nd
					heap.Push(h, st{to, cur.hops + 1, nd})
				}
			}
		}
	}
	return -1
}
