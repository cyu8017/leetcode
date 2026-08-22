// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

import "container/heap"

type appleEdge3928 struct {
	to, empty, full int
}
type appleState3928 struct {
	node int
	dist int64
}
type appleHeap3928 []appleState3928

func (h appleHeap3928) Len() int            { return len(h) }
func (h appleHeap3928) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h appleHeap3928) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *appleHeap3928) Push(x interface{}) { *h = append(*h, x.(appleState3928)) }
func (h *appleHeap3928) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func minCostToBuyApples(n int, prices []int, roads [][]int) []int64 {
	g := make([][]appleEdge3928, n)
	for _, road := range roads {
		e := appleEdge3928{road[1], road[2], road[2] * road[3]}
		g[road[0]] = append(g[road[0]], e)
		e.to = road[0]
		g[road[1]] = append(g[road[1]], e)
	}
	dijkstra := func(source int, carrying bool) []int64 {
		const inf int64 = 1 << 62
		dist := make([]int64, n)
		for i := range dist {
			dist[i] = inf
		}
		dist[source] = 0
		pq := &appleHeap3928{{source, 0}}
		heap.Init(pq)
		for pq.Len() > 0 {
			cur := heap.Pop(pq).(appleState3928)
			if cur.dist != dist[cur.node] {
				continue
			}
			for _, e := range g[cur.node] {
				weight := e.empty
				if carrying {
					weight = e.full
				}
				next := cur.dist + int64(weight)
				if next < dist[e.to] {
					dist[e.to] = next
					heap.Push(pq, appleState3928{e.to, next})
				}
			}
		}
		return dist
	}
	answer := make([]int64, n)
	for source := 0; source < n; source++ {
		emptyDist, fullDist := dijkstra(source, false), dijkstra(source, true)
		best := int64(prices[source])
		for shop := 0; shop < n; shop++ {
			if emptyDist[shop] == 1<<62 || fullDist[shop] == 1<<62 {
				continue
			}
			total := emptyDist[shop] + fullDist[shop] + int64(prices[shop])
			if total < best {
				best = total
			}
		}
		answer[source] = best
	}
	return answer
}