// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

import "container/heap"

type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func earliestSecondToMarkIndices(nums []int, changeIndices []int) int {
	secondToIndex := getSecondToIndex(nums, changeIndices)
	var numsSum int64
	for _, v := range nums {
		numsSum += int64(v)
	}
	l, r := 0, len(changeIndices)+1
	for l < r {
		m := (l + r) / 2
		if canMark(nums, secondToIndex, m, numsSum) {
			r = m
		} else {
			l = m + 1
		}
	}
	if l <= len(changeIndices) {
		return l
	}
	return -1
}

func canMark(nums []int, secondToIndex map[int]int, maxSecond int, numsSum int64) bool {
	h := &minHeap{}
	heap.Init(h)
	marks := 0
	for second := maxSecond - 1; second >= 0; second-- {
		if index, ok := secondToIndex[second]; ok {
			heap.Push(h, nums[index])
			if marks == 0 {
				heap.Pop(h)
				marks++
			} else {
				marks--
			}
		} else {
			marks++
		}
	}
	heapSize := h.Len()
	var heapSum int64
	for h.Len() > 0 {
		heapSum += int64(heap.Pop(h).(int))
	}
	decrementAndMarkCost := numsSum - heapSum + int64(len(nums)-heapSize)
	zeroAndMarkCost := int64(heapSize + heapSize)
	return decrementAndMarkCost+zeroAndMarkCost <= int64(maxSecond)
}

func getSecondToIndex(nums []int, changeIndices []int) map[int]int {
	indexToFirstSecond := map[int]int{}
	for second, oneIndexed := range changeIndices {
		index := oneIndexed - 1
		if nums[index] > 0 {
			if _, ok := indexToFirstSecond[index]; !ok {
				indexToFirstSecond[index] = second
			}
		}
	}
	secondToIndex := map[int]int{}
	for index, second := range indexToFirstSecond {
		secondToIndex[second] = index
	}
	return secondToIndex
}
