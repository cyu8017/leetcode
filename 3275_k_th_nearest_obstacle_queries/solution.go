// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

import "container/heap"

type maxH []int

func (h maxH) Len() int            { return len(h) }
func (h maxH) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func resultsArray(queries [][]int, k int) []int {
	h := &maxH{}
	ans := make([]int, len(queries))
	for i, q := range queries {
		d := q[0]
		if d < 0 {
			d = -d
		}
		if q[1] < 0 {
			d += -q[1]
		} else {
			d += q[1]
		}
		heap.Push(h, d)
		if h.Len() > k {
			heap.Pop(h)
		}
		if h.Len() < k {
			ans[i] = -1
		} else {
			ans[i] = (*h)[0]
		}
	}
	return ans
}
