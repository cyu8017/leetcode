// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

import "container/heap"
import "sort"

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

func maxRemoval(nums []int, queries [][]int) int {
	sort.Slice(queries, func(i, j int) bool { return queries[i][0] < queries[j][0] })
	h := &maxH{}
	n := len(nums)
	diff := make([]int, n+1)
	j, used, cur := 0, 0, 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		for j < len(queries) && queries[j][0] == i {
			heap.Push(h, queries[j][1])
			j++
		}
		for cur < nums[i] {
			if h.Len() == 0 || (*h)[0] < i {
				return -1
			}
			r := heap.Pop(h).(int)
			cur++
			diff[r+1]--
			used++
		}
	}
	return len(queries) - used
}
