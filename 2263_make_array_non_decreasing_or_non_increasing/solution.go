// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func convertArray(nums []int) int {
	cost := func(arr []int) int {
		h := &IntHeap{}
		heap.Init(h)
		ans := 0
		for _, x := range arr {
			if h.Len() > 0 && (*h)[0] > x {
				ans += (*h)[0] - x
				heap.Pop(h)
				heap.Push(h, x)
			}
			heap.Push(h, x)
		}
		return ans
	}
	rev := make([]int, len(nums))
	for i, v := range nums {
		rev[len(nums)-1-i] = v
	}
	a, b := cost(nums), cost(rev)
	if a < b {
		return a
	}
	return b
}
