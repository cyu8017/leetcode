// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/


import "container/heap"

type ei struct{ node, dist int }
type eh []ei
func (h eh) Len() int            { return len(h) }
func (h eh) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h eh) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *eh) Push(x interface{}) { *h = append(*h, x.(ei)) }
func (h *eh) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumDistance(n int, edges [][]int, s int, marked []int) int {
	g := make([][][2]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], [2]int{e[1], e[2]})
	}
	mark := map[int]bool{}
	for _, x := range marked {
		mark[x] = true
	}
	dist := make([]int, n)
	for i := range dist {
		dist[i] = 1 << 30
	}
	dist[s] = 0
	h := &eh{{s, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(ei)
		if mark[cur.node] {
			return cur.dist
		}
		if cur.dist > dist[cur.node] {
			continue
		}
		for _, e := range g[cur.node] {
			nd := cur.dist + e[1]
			if nd < dist[e[0]] {
				dist[e[0]] = nd
				heap.Push(h, ei{e[0], nd})
			}
		}
	}
	return -1
}
