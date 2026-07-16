// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import "container/heap"

type pairEntry struct {
	sum    int
	index1 int
	index2 int
}

type pairHeap []pairEntry

func (h pairHeap) Len() int            { return len(h) }
func (h pairHeap) Less(i, j int) bool  { return h[i].sum < h[j].sum }
func (h pairHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pairHeap) Push(x interface{}) { *h = append(*h, x.(pairEntry)) }
func (h *pairHeap) Pop() interface{} {
	items := *h
	item := items[len(items)-1]
	*h = items[:len(items)-1]
	return item
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	if len(nums1) == 0 || len(nums2) == 0 || k == 0 {
		return nil
	}

	minHeap := make(pairHeap, 0)
	heap.Init(&minHeap)
	limit := len(nums1)
	if limit > k {
		limit = k
	}
	for index := 0; index < limit; index++ {
		heap.Push(&minHeap, pairEntry{sum: nums1[index] + nums2[0], index1: index, index2: 0})
	}

	result := make([][]int, 0, k)
	for len(minHeap) > 0 && len(result) < k {
		top := heap.Pop(&minHeap).(pairEntry)
		result = append(result, []int{nums1[top.index1], nums2[top.index2]})
		if top.index2+1 < len(nums2) {
			heap.Push(&minHeap, pairEntry{
				sum:    nums1[top.index1] + nums2[top.index2+1],
				index1: top.index1,
				index2: top.index2 + 1,
			})
		}
	}

	return result
}
