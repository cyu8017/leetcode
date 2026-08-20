// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

import "container/heap"

type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	stations = append(append([][]int{}, stations...), []int{target, 0})
	pq := &maxHeap{}
	heap.Init(pq)
	ans, prev, fuel := 0, 0, startFuel
	for _, st := range stations {
		pos, gas := st[0], st[1]
		fuel -= pos - prev
		for pq.Len() > 0 && fuel < 0 {
			fuel += heap.Pop(pq).(int)
			ans++
		}
		if fuel < 0 {
			return -1
		}
		heap.Push(pq, gas)
		prev = pos
	}
	return ans
}
