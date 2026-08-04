// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

import "container/heap"

type mcItem struct {
	cost, time, node int
}

type mcHeap []mcItem

func (h mcHeap) Len() int            { return len(h) }
func (h mcHeap) Less(i, j int) bool  { return h[i].cost < h[j].cost }
func (h mcHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *mcHeap) Push(x interface{}) { *h = append(*h, x.(mcItem)) }
func (h *mcHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minCost(maxTime int, edges [][]int, passingFee []int) int {
	n := len(passingFee)
	graph := make([][][2]int, n)
	for _, e := range edges {
		u, v, t := e[0], e[1], e[2]
		graph[u] = append(graph[u], [2]int{v, t})
		graph[v] = append(graph[v], [2]int{u, t})
	}
	minTime := make([]int, n)
	for i := range minTime {
		minTime[i] = maxTime + 1
	}
	h := &mcHeap{{passingFee[0], 0, 0}}
	heap.Init(h)
	for h.Len() > 0 {
		cur := heap.Pop(h).(mcItem)
		if cur.time >= minTime[cur.node] {
			continue
		}
		minTime[cur.node] = cur.time
		if cur.node == n-1 {
			return cur.cost
		}
		for _, e := range graph[cur.node] {
			v, dt := e[0], e[1]
			nt := cur.time + dt
			if nt <= maxTime && nt < minTime[v] {
				heap.Push(h, mcItem{cur.cost + passingFee[v], nt, v})
			}
		}
	}
	return -1
}
