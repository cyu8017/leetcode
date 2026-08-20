// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

import "container/heap"

type edge struct{ to, w int }
type item struct{ node int; dist int64 }
type PQ []item

func (h PQ) Len() int            { return len(h) }
func (h PQ) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h PQ) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *PQ) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *PQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minCost(n int, roads [][]int, appleCost []int, k int) []int64 {
	g := make([][]edge, n+1)
	for _, r := range roads {
		g[r[0]] = append(g[r[0]], edge{r[1], r[2]})
		g[r[1]] = append(g[r[1]], edge{r[0], r[2]})
	}
	ans := make([]int64, n)
	for start := 1; start <= n; start++ {
		dist := make([]int64, n+1)
		for i := range dist {
			dist[i] = 1 << 60
		}
		dist[start] = 0
		h := &PQ{{start, 0}}
		heap.Init(h)
		for h.Len() > 0 {
			cur := heap.Pop(h).(item)
			if cur.dist != dist[cur.node] {
				continue
			}
			for _, e := range g[cur.node] {
				nd := cur.dist + int64(e.w)
				if nd < dist[e.to] {
					dist[e.to] = nd
					heap.Push(h, item{e.to, nd})
				}
			}
		}
		best := int64(1 << 60)
		for city := 1; city <= n; city++ {
			cost := dist[city]*int64(k+1) + int64(appleCost[city-1])
			if cost < best {
				best = cost
			}
		}
		ans[start-1] = best
	}
	return ans
}
