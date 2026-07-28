// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

import "container/heap"

type maxHeap1046 []int

func (h maxHeap1046) Len() int            { return len(h) }
func (h maxHeap1046) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap1046) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap1046) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap1046) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func lastStoneWeight(stones []int) int {
	h := maxHeap1046(append([]int{}, stones...))
	heap.Init(&h)
	for h.Len() > 1 {
		a := heap.Pop(&h).(int)
		b := heap.Pop(&h).(int)
		if a != b {
			heap.Push(&h, a-b)
		}
	}
	if h.Len() == 0 {
		return 0
	}
	return h[0]
}
