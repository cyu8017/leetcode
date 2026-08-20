// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type NumberContainers struct {
	idx  map[int]int
	heap map[int]*IntHeap
}

func Constructor() NumberContainers {
	return NumberContainers{idx: map[int]int{}, heap: map[int]*IntHeap{}}
}

func (this *NumberContainers) Change(index int, number int) {
	this.idx[index] = number
	if this.heap[number] == nil {
		h := &IntHeap{}
		heap.Init(h)
		this.heap[number] = h
	}
	heap.Push(this.heap[number], index)
}

func (this *NumberContainers) Find(number int) int {
	h := this.heap[number]
	if h == nil {
		return -1
	}
	for h.Len() > 0 {
		i := (*h)[0]
		if this.idx[i] == number {
			return i
		}
		heap.Pop(h)
	}
	return -1
}
