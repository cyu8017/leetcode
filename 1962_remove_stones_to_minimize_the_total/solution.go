// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import "container/heap"

type maxHeap1962 []int

func (h maxHeap1962) Len() int            { return len(h) }
func (h maxHeap1962) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap1962) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap1962) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap1962) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minStoneSum(piles []int, k int) int {
	h := maxHeap1962(append([]int{}, piles...))
	heap.Init(&h)
	for i := 0; i < k; i++ {
		x := heap.Pop(&h).(int)
		heap.Push(&h, x-x/2)
	}
	sum := 0
	for _, v := range h {
		sum += v
	}
	return sum
}
