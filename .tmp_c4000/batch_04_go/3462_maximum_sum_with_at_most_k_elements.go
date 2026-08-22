// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

import "container/heap"
import "sort"

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

func maxSum(grid [][]int, limits []int, k int) int64 {
	h := &minH{}
	var sum int64
	for i, row := range grid {
		r := append([]int(nil), row...)
		sort.Sort(sort.Reverse(sort.IntSlice(r)))
		lim := limits[i]
		if lim > len(r) {
			lim = len(r)
		}
		for j := 0; j < lim; j++ {
			heap.Push(h, r[j])
			sum += int64(r[j])
			if h.Len() > k {
				sum -= int64(heap.Pop(h).(int))
			}
		}
	}
	return sum
}
