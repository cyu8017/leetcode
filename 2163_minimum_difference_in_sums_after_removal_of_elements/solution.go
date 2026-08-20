// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

import "container/heap"

type maxH2163 []int
type minH2163 []int

func (h maxH2163) Len() int            { return len(h) }
func (h maxH2163) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxH2163) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxH2163) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxH2163) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}
func (h minH2163) Len() int            { return len(h) }
func (h minH2163) Less(i, j int) bool  { return h[i] < h[j] }
func (h minH2163) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH2163) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minH2163) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func minimumDifference(nums []int) int64 {
	n := len(nums) / 3
	left := make([]int64, len(nums))
	right := make([]int64, len(nums))
	hmax := &maxH2163{}
	var sum int64
	for i := 0; i < n; i++ {
		heap.Push(hmax, nums[i])
		sum += int64(nums[i])
	}
	left[n-1] = sum
	for i := n; i < 2*n; i++ {
		heap.Push(hmax, nums[i])
		sum += int64(nums[i])
		sum -= int64(heap.Pop(hmax).(int))
		left[i] = sum
	}
	hmin := &minH2163{}
	sum = 0
	for i := len(nums) - 1; i >= 2*n; i-- {
		heap.Push(hmin, nums[i])
		sum += int64(nums[i])
	}
	right[2*n] = sum
	for i := 2*n - 1; i >= n; i-- {
		heap.Push(hmin, nums[i])
		sum += int64(nums[i])
		sum -= int64(heap.Pop(hmin).(int))
		right[i] = sum
	}
	ans := left[n-1] - right[n]
	for i := n; i < 2*n; i++ {
		diff := left[i] - right[i+1]
		if diff < ans {
			ans = diff
		}
	}
	return ans
}
