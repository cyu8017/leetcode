// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

import "container/heap"

type minH []int

func (h minH) Len() int            { return len(h) }
func (h minH) Less(i, j int) bool  { return h[i] < h[j] }
func (h minH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minBuildTime(blocks []int, split int) int {
	h := minH(append([]int{}, blocks...))
	heap.Init(&h)
	for h.Len() > 1 {
		heap.Pop(&h)
		b := heap.Pop(&h).(int)
		heap.Push(&h, b+split)
	}
	return h[0]
}
