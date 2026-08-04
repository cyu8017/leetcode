// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

import "container/heap"

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type DinnerPlates struct {
	capacity int
	stacks   [][]int
	avail    intHeap
	inAvail  map[int]bool
}

func Constructor(capacity int) DinnerPlates {
	return DinnerPlates{
		capacity: capacity,
		avail:    intHeap{},
		inAvail:  map[int]bool{},
	}
}

func (this *DinnerPlates) Push(val int) {
	for this.avail.Len() > 0 {
		idx := this.avail[0]
		if idx < len(this.stacks) && len(this.stacks[idx]) < this.capacity {
			break
		}
		heap.Pop(&this.avail)
		delete(this.inAvail, idx)
	}
	if this.avail.Len() == 0 {
		this.stacks = append(this.stacks, []int{})
		heap.Push(&this.avail, len(this.stacks)-1)
		this.inAvail[len(this.stacks)-1] = true
	}
	idx := this.avail[0]
	this.stacks[idx] = append(this.stacks[idx], val)
	if len(this.stacks[idx]) == this.capacity {
		heap.Pop(&this.avail)
		delete(this.inAvail, idx)
	}
}

func (this *DinnerPlates) Pop() int {
	return this.PopAtStack(len(this.stacks) - 1)
}

func (this *DinnerPlates) PopAtStack(index int) int {
	if index < 0 || index >= len(this.stacks) || len(this.stacks[index]) == 0 {
		return -1
	}
	st := this.stacks[index]
	val := st[len(st)-1]
	this.stacks[index] = st[:len(st)-1]
	if !this.inAvail[index] {
		heap.Push(&this.avail, index)
		this.inAvail[index] = true
	}
	for len(this.stacks) > 0 && len(this.stacks[len(this.stacks)-1]) == 0 {
		last := len(this.stacks) - 1
		this.stacks = this.stacks[:last]
		if this.inAvail[last] {
			delete(this.inAvail, last)
		}
	}
	return val
}
