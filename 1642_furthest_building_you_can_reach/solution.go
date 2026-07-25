// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

import "container/heap"

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
	climbs := &intHeap{}
	heap.Init(climbs)
	for i := 0; i+1 < len(heights); i++ {
		d := heights[i+1] - heights[i]
		if d <= 0 {
			continue
		}
		heap.Push(climbs, d)
		if climbs.Len() > ladders {
			bricks -= heap.Pop(climbs).(int)
		}
		if bricks < 0 {
			return i
		}
	}
	return len(heights) - 1
}
