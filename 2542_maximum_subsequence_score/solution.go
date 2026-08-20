// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/


import container/heap
import sort

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

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return nums2[idx[i]] > nums2[idx[j]] })
	h := &minH{}
	heap.Init(h)
	var sum, ans int64
	for _, i := range idx {
		heap.Push(h, nums1[i])
		sum += int64(nums1[i])
		if h.Len() > k {
			sum -= int64(heap.Pop(h).(int))
		}
		if h.Len() == k {
			cand := sum * int64(nums2[i])
			if cand > ans {
				ans = cand
			}
		}
	}
	return ans
}
