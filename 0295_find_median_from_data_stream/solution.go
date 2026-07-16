// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

import "container/heap"

type IntMaxHeap []int

func (h IntMaxHeap) Len() int            { return len(h) }
func (h IntMaxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h IntMaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntMaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntMaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

type IntMinHeap []int

func (h IntMinHeap) Len() int            { return len(h) }
func (h IntMinHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntMinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntMinHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

type MedianFinder struct {
	small *IntMaxHeap
	large *IntMinHeap
}

func Constructor() MedianFinder {
	small := IntMaxHeap{}
	large := IntMinHeap{}
	heap.Init(&small)
	heap.Init(&large)
	return MedianFinder{small: &small, large: &large}
}

func (this *MedianFinder) AddNum(num int) {
	heap.Push(this.small, num)
	heap.Push(this.large, heap.Pop(this.small))
	if this.large.Len() > this.small.Len() {
		heap.Push(this.small, heap.Pop(this.large))
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.small.Len() > this.large.Len() {
		return float64((*this.small)[0])
	}
	return float64((*this.small)[0]+(*this.large)[0]) / 2.0
}
