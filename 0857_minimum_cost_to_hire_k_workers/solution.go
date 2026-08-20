// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import (
	"container/heap"
	"math"
	"sort"
)

type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
	type worker struct{ ratio float64; q int }
	workers := make([]worker, len(quality))
	for i := range quality {
		workers[i] = worker{float64(wage[i]) / float64(quality[i]), quality[i]}
	}
	sort.Slice(workers, func(i, j int) bool { return workers[i].ratio < workers[j].ratio })
	h := &maxHeap{}
	heap.Init(h)
	totalQ := 0
	ans := math.Inf(1)
	for _, w := range workers {
		heap.Push(h, w.q)
		totalQ += w.q
		if h.Len() > k {
			totalQ -= heap.Pop(h).(int)
		}
		if h.Len() == k {
			cost := float64(totalQ) * w.ratio
			if cost < ans {
				ans = cost
			}
		}
	}
	return ans
}
