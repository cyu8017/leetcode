// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

import (
	"container/heap"
	"sort"
)

type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxPerformance(n int, speed []int, efficiency []int, k int) int {
	type pair struct{ e, s int }
	people := make([]pair, n)
	for i := 0; i < n; i++ {
		people[i] = pair{efficiency[i], speed[i]}
	}
	sort.Slice(people, func(i, j int) bool { return people[i].e > people[j].e })
	h := &minHeap{}
	heap.Init(h)
	total, ans := 0, 0
	for _, p := range people {
		heap.Push(h, p.s)
		total += p.s
		if h.Len() > k {
			total -= heap.Pop(h).(int)
		}
		perf := total * p.e
		if perf > ans {
			ans = perf
		}
	}
	return ans % 1000000007
}
