// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

import "container/heap"

type frac struct {
	val float64
	i, j int
}
type fracHeap []frac

func (h fracHeap) Len() int            { return len(h) }
func (h fracHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h fracHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *fracHeap) Push(x interface{}) { *h = append(*h, x.(frac)) }
func (h *fracHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
	n := len(arr)
	h := &fracHeap{}
	heap.Init(h)
	for i := 0; i < n-1; i++ {
		heap.Push(h, frac{float64(arr[i]) / float64(arr[n-1]), i, n - 1})
	}
	for t := 0; t < k-1; t++ {
		cur := heap.Pop(h).(frac)
		if cur.j-1 > cur.i {
			heap.Push(h, frac{float64(arr[cur.i]) / float64(arr[cur.j-1]), cur.i, cur.j - 1})
		}
	}
	cur := heap.Pop(h).(frac)
	return []int{arr[cur.i], arr[cur.j]}
}
