// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

import "container/heap"

type worker struct{ idx, efficiency, leftToRight, pickOld, rightToLeft, putNew int }
type waitHeap []worker

func (h waitHeap) Len() int { return len(h) }
func (h waitHeap) Less(i, j int) bool {
	if h[i].efficiency != h[j].efficiency {
		return h[i].efficiency > h[j].efficiency
	}
	return h[i].idx > h[j].idx
}
func (h waitHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *waitHeap) Push(x interface{}) { *h = append(*h, x.(worker)) }
func (h *waitHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type event struct{ time int; w worker; side int } // side 0 left arrive, 1 right arrive
type eventHeap []event

func (h eventHeap) Len() int            { return len(h) }
func (h eventHeap) Less(i, j int) bool  { return h[i].time < h[j].time }
func (h eventHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *eventHeap) Push(x interface{}) { *h = append(*h, x.(event)) }
func (h *eventHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func findCrossingTime(n int, k int, time [][]int) int {
	left := &waitHeap{}
	right := &waitHeap{}
	heap.Init(left)
	heap.Init(right)
	for i := 0; i < k; i++ {
		w := worker{i, time[i][0] + time[i][2], time[i][0], time[i][1], time[i][2], time[i][3]}
		heap.Push(left, w)
	}
	events := &eventHeap{}
	heap.Init(events)
	cur, remain, done := 0, n, 0
	bridgeFree := 0
	for done < n {
		for events.Len() > 0 && (*events)[0].time <= cur {
			e := heap.Pop(events).(event)
			if e.side == 0 {
				heap.Push(left, e.w)
			} else {
				heap.Push(right, e.w)
			}
		}
		if cur < bridgeFree {
			cur = bridgeFree
			continue
		}
		if right.Len() > 0 {
			w := heap.Pop(right).(worker)
			cur += w.rightToLeft
			bridgeFree = cur
			heap.Push(events, event{cur + w.putNew, w, 0})
			done++
			continue
		}
		if left.Len() > 0 && remain > 0 {
			w := heap.Pop(left).(worker)
			cur += w.leftToRight
			bridgeFree = cur
			remain--
			heap.Push(events, event{cur + w.pickOld, w, 1})
			continue
		}
		if events.Len() == 0 {
			break
		}
		cur = (*events)[0].time
	}
	return cur
}
