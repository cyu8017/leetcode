// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

import "container/heap"
import "sort"

type mh3478 []int

func (h mh3478) Len() int            { return len(h) }
func (h mh3478) Less(i, j int) bool  { return h[i] < h[j] }
func (h mh3478) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *mh3478) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *mh3478) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func findMaxSum(nums1 []int, nums2 []int, k int) []int64 {
	n := len(nums1)
	type item struct{ v1, v2, i int }
	arr := make([]item, n)
	for i := range nums1 {
		arr[i] = item{nums1[i], nums2[i], i}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].v1 < arr[j].v1 })
	ans := make([]int64, n)
	h := &mh3478{}
	var sum int64
	j := 0
	for i := 0; i < n; {
		v := arr[i].v1
		start := i
		for i < n && arr[i].v1 == v {
			i++
		}
		// all with smaller nums1 already in heap
		for t := start; t < i; t++ {
			ans[arr[t].i] = sum
		}
		for t := start; t < i; t++ {
			heap.Push(h, arr[t].v2)
			sum += int64(arr[t].v2)
			if h.Len() > k {
				sum -= int64(heap.Pop(h).(int))
			}
		}
		_ = j
	}
	return ans
}
