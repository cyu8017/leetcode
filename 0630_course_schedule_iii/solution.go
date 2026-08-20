// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

import (
	"container/heap"
	"sort"
)

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

func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool { return courses[i][1] < courses[j][1] })
	h := &maxHeap{}
	heap.Init(h)
	time := 0
	for _, course := range courses {
		duration, lastDay := course[0], course[1]
		if time+duration <= lastDay {
			heap.Push(h, duration)
			time += duration
		} else if h.Len() > 0 && (*h)[0] > duration {
			time += duration - heap.Pop(h).(int)
			heap.Push(h, duration)
		}
	}
	return h.Len()
}
