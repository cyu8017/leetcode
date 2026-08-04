// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

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

func maxEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool { return events[i][0] < events[j][0] })
	h := &minHeap{}
	heap.Init(h)
	i, ans, day := 0, 0, 0
	for i < len(events) || h.Len() > 0 {
		if h.Len() == 0 {
			if day < events[i][0] {
				day = events[i][0]
			}
		}
		for i < len(events) && events[i][0] <= day {
			heap.Push(h, events[i][1])
			i++
		}
		for h.Len() > 0 && (*h)[0] < day {
			heap.Pop(h)
		}
		if h.Len() > 0 {
			heap.Pop(h)
			ans++
			day++
		}
	}
	return ans
}
