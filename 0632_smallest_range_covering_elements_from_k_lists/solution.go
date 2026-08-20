// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import "container/heap"

type item struct {
	value, listIndex, index int
}

type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].value < h[j].value }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func smallestRange(nums [][]int) []int {
	h := &minHeap{}
	heap.Init(h)
	currentMax := -1 << 31
	for i, arr := range nums {
		heap.Push(h, item{arr[0], i, 0})
		if arr[0] > currentMax {
			currentMax = arr[0]
		}
	}
	bestLeft, bestRight := (*h)[0].value, currentMax
	for {
		cur := heap.Pop(h).(item)
		if currentMax-cur.value < bestRight-bestLeft {
			bestLeft, bestRight = cur.value, currentMax
		}
		if cur.index+1 == len(nums[cur.listIndex]) {
			break
		}
		nxt := nums[cur.listIndex][cur.index+1]
		heap.Push(h, item{nxt, cur.listIndex, cur.index + 1})
		if nxt > currentMax {
			currentMax = nxt
		}
	}
	return []int{bestLeft, bestRight}
}
