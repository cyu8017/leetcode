// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

import "container/heap"

type item2203 struct{ dist int64; node int }
type pq2203 []item2203

func (p pq2203) Len() int            { return len(p) }
func (p pq2203) Less(i, j int) bool  { return p[i].dist < p[j].dist }
func (p pq2203) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *pq2203) Push(x interface{}) { *p = append(*p, x.(item2203)) }
func (p *pq2203) Pop() interface{} {
	old := *p
	x := old[len(old)-1]
	*p = old[:len(old)-1]
	return x
}

func dijkstra2203(n int, g [][][2]int, src int) []int64 {
	dist := make([]int64, n)
	for i := range dist {
		dist[i] = 1 << 62
	}
	dist[src] = 0
	h := &pq2203{{0, src}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(item2203)
		if cur.dist != dist[cur.node] {
			continue
		}
		for _, e := range g[cur.node] {
			v, w := e[0], int64(e[1])
			if cur.dist+w < dist[v] {
				dist[v] = cur.dist + w
				heap.Push(h, item2203{dist[v], v})
			}
		}
	}
	return dist
}

func minimumWeight(n int, edges [][]int, src1 int, src2 int, dest int) int64 {
	g := make([][][2]int, n)
	rg := make([][][2]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], [2]int{e[1], e[2]})
		rg[e[1]] = append(rg[e[1]], [2]int{e[0], e[2]})
	}
	d1 := dijkstra2203(n, g, src1)
	d2 := dijkstra2203(n, g, src2)
	dd := dijkstra2203(n, rg, dest)
	ans := int64(1 << 62)
	for i := 0; i < n; i++ {
		if d1[i] >= 1<<62 || d2[i] >= 1<<62 || dd[i] >= 1<<62 {
			continue
		}
		cand := d1[i] + d2[i] + dd[i]
		if cand < ans {
			ans = cand
		}
	}
	if ans >= 1<<62 {
		return -1
	}
	return ans
}
