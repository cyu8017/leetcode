// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/


import "container/heap"

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

func makePrefSumNonNegative(nums []int) int {
	h := &minH{}
	heap.Init(h)
	sum, ans := int64(0), 0
	for _, x := range nums {
		sum += int64(x)
		if x < 0 {
			heap.Push(h, x)
		}
		if sum < 0 {
			worst := heap.Pop(h).(int)
			sum -= int64(worst)
			ans++
		}
	}
	return ans
}
