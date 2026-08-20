// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

import (
	"container/heap"
	"sort"
)

type int64Heap []int64

func (h int64Heap) Len() int            { return len(h) }
func (h int64Heap) Less(i, j int) bool  { return h[i] < h[j] }
func (h int64Heap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *int64Heap) Push(x interface{}) { *h = append(*h, x.(int64)) }
func (h *int64Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type roomHeap [][2]int64 // end, room

func (h roomHeap) Len() int { return len(h) }
func (h roomHeap) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}
	return h[i][0] < h[j][0]
}
func (h roomHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *roomHeap) Push(x interface{}) { *h = append(*h, x.([2]int64)) }
func (h *roomHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool { return meetings[i][0] < meetings[j][0] })
	free := &int64Heap{}
	heap.Init(free)
	for i := 0; i < n; i++ {
		heap.Push(free, int64(i))
	}
	busy := &roomHeap{}
	heap.Init(busy)
	cnt := make([]int, n)
	for _, m := range meetings {
		start, end := int64(m[0]), int64(m[1])
		for busy.Len() > 0 && (*busy)[0][0] <= start {
			room := heap.Pop(busy).([2]int64)[1]
			heap.Push(free, room)
		}
		dur := end - start
		var room int64
		var begin int64
		if free.Len() > 0 {
			room = heap.Pop(free).(int64)
			begin = start
		} else {
			top := heap.Pop(busy).([2]int64)
			begin = top[0]
			room = top[1]
		}
		heap.Push(busy, [2]int64{begin + dur, room})
		cnt[room]++
	}
	ans := 0
	for i := 1; i < n; i++ {
		if cnt[i] > cnt[ans] {
			ans = i
		}
	}
	return ans
}
