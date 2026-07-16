// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

import (
	"container/heap"
	"sort"
)

type heapItem struct {
	negH int
	end  int
}

type minHeap []heapItem

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].negH < h[j].negH }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(heapItem)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func getSkyline(buildings [][]int) [][]int {
	type event struct {
		x, negH, end int
	}
	events := make([]event, 0, len(buildings)*2)
	for _, building := range buildings {
		events = append(events, event{building[0], -building[2], building[1]})
		events = append(events, event{building[1], 0, 0})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].x != events[j].x {
			return events[i].x < events[j].x
		}
		return events[i].negH < events[j].negH
	})

	result := make([][]int, 0)
	live := &minHeap{{0, 1 << 30}}
	heap.Init(live)

	for _, ev := range events {
		for live.Len() > 0 && (*live)[0].end <= ev.x {
			heap.Pop(live)
		}
		if ev.negH != 0 {
			heap.Push(live, heapItem{ev.negH, ev.end})
		}
		height := -(*live)[0].negH
		if len(result) == 0 || result[len(result)-1][1] != height {
			result = append(result, []int{ev.x, height})
		}
	}
	return result
}
