// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import (
	"container/heap"
	"sort"
)

type intMinHeap []int

func (h intMinHeap) Len() int            { return len(h) }
func (h intMinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intMinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intMinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type leaveItem struct{ leave, chair int }
type leaveHeap []leaveItem

func (h leaveHeap) Len() int            { return len(h) }
func (h leaveHeap) Less(i, j int) bool  { return h[i].leave < h[j].leave }
func (h leaveHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *leaveHeap) Push(x interface{}) { *h = append(*h, x.(leaveItem)) }
func (h *leaveHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func smallestChair(times [][]int, targetFriend int) int {
	order := make([]int, len(times))
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		return times[order[i]][0] < times[order[j]][0]
	})
	free := &intMinHeap{}
	heap.Init(free)
	nextChair := 0
	leaving := &leaveHeap{}
	heap.Init(leaving)
	for _, i := range order {
		arr, leave := times[i][0], times[i][1]
		for leaving.Len() > 0 && (*leaving)[0].leave <= arr {
			heap.Push(free, heap.Pop(leaving).(leaveItem).chair)
		}
		var chair int
		if free.Len() > 0 {
			chair = heap.Pop(free).(int)
		} else {
			chair = nextChair
			nextChair++
		}
		if i == targetFriend {
			return chair
		}
		heap.Push(leaving, leaveItem{leave, chair})
	}
	return -1
}
