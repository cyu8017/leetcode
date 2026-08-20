// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

import "container/heap"

type miPair struct{ v, i int }
type miHeap []miPair

func (h miHeap) Len() int { return len(h) }
func (h miHeap) Less(i, j int) bool {
	if h[i].v == h[j].v {
		return h[i].i < h[j].i
	}
	return h[i].v < h[j].v
}
func (h miHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *miHeap) Push(x interface{}) { *h = append(*h, x.(miPair)) }
func (h *miHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func getFinalState(nums []int, k int, multiplier int) []int {
	h := &miHeap{}
	for i, v := range nums {
		heap.Push(h, miPair{v, i})
	}
	for t := 0; t < k; t++ {
		p := heap.Pop(h).(miPair)
		p.v *= multiplier
		nums[p.i] = p.v
		heap.Push(h, p)
	}
	return nums
}
