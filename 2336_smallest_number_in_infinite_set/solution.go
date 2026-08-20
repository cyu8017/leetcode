// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

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

type SmallestInfiniteSet struct {
	next    int
	added   map[int]bool
	heap    IntHeap
}

func Constructor() SmallestInfiniteSet {
	h := IntHeap{}
	heap.Init(&h)
	return SmallestInfiniteSet{next: 1, added: map[int]bool{}, heap: h}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	if this.heap.Len() > 0 {
		x := heap.Pop(&this.heap).(int)
		delete(this.added, x)
		return x
	}
	x := this.next
	this.next++
	return x
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num < this.next && !this.added[num] {
		this.added[num] = true
		heap.Push(&this.heap, num)
	}
}
