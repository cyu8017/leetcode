// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

import "container/heap"

type probItem struct {
	prob float64
	node int
}

type maxHeap []probItem

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].prob > h[j].prob }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(probItem)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
	graph := make([][]struct {
		to   int
		prob float64
	}, n)
	for i, e := range edges {
		a, b := e[0], e[1]
		p := succProb[i]
		graph[a] = append(graph[a], struct {
			to   int
			prob float64
		}{b, p})
		graph[b] = append(graph[b], struct {
			to   int
			prob float64
		}{a, p})
	}
	best := make([]float64, n)
	best[start_node] = 1
	h := &maxHeap{{1, start_node}}
	heap.Init(h)
	for h.Len() > 0 {
		item := heap.Pop(h).(probItem)
		if item.node == end_node {
			return item.prob
		}
		if item.prob < best[item.node] {
			continue
		}
		for _, edge := range graph[item.node] {
			candidate := item.prob * edge.prob
			if candidate > best[edge.to] {
				best[edge.to] = candidate
				heap.Push(h, probItem{candidate, edge.to})
			}
		}
	}
	return 0
}
