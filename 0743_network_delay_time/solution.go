// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

import "container/heap"

type item struct{ d, node int }
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].d < h[j].d }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func networkDelayTime(times [][]int, n int, k int) int {
	graph := make([][][2]int, n+1)
	for _, t := range times {
		u, v, w := t[0], t[1], t[2]
		graph[u] = append(graph[u], [2]int{v, w})
	}
	const inf = int(1e18)
	dist := make([]int, n+1)
	for i := range dist {
		dist[i] = inf
	}
	dist[k] = 0
	h := &minHeap{{0, k}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.d > dist[cur.node] {
			continue
		}
		for _, edge := range graph[cur.node] {
			nd := cur.d + edge[1]
			if nd < dist[edge[0]] {
				dist[edge[0]] = nd
				heap.Push(h, item{nd, edge[0]})
			}
		}
	}
	ans := 0
	for i := 1; i <= n; i++ {
		if dist[i] == inf {
			return -1
		}
		if dist[i] > ans {
			ans = dist[i]
		}
	}
	return ans
}
