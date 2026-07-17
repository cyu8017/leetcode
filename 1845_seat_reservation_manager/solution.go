// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

import "container/heap"

type SeatManager struct {
	available intHeap
}

func Constructor(n int) SeatManager {
	h := make(intHeap, n)
	for i := 0; i < n; i++ {
		h[i] = i + 1
	}
	heap.Init(&h)
	return SeatManager{available: h}
}

func (this *SeatManager) Reserve() int {
	return heap.Pop(&this.available).(int)
}

func (this *SeatManager) Unreserve(seatNumber int) {
	heap.Push(&this.available, seatNumber)
}

type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}
