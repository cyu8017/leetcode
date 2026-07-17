// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

import (
	"container/heap"
	"sort"
)

type taskInfo struct {
	index    int
	enqueue  int
	duration int
}

type taskHeap []taskInfo

func (h taskHeap) Len() int { return len(h) }
func (h taskHeap) Less(i, j int) bool {
	if h[i].duration != h[j].duration {
		return h[i].duration < h[j].duration
	}
	return h[i].index < h[j].index
}
func (h taskHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *taskHeap) Push(x interface{}) {
	*h = append(*h, x.(taskInfo))
}
func (h *taskHeap) Pop() interface{} {
	old := *h
	item := old[len(old)-1]
	*h = old[:len(old)-1]
	return item
}

func getOrder(tasks [][]int) []int {
	indexed := make([]taskInfo, len(tasks))
	for i, task := range tasks {
		indexed[i] = taskInfo{index: i, enqueue: task[0], duration: task[1]}
	}
	sort.Slice(indexed, func(i, j int) bool {
		if indexed[i].enqueue != indexed[j].enqueue {
			return indexed[i].enqueue < indexed[j].enqueue
		}
		return indexed[i].index < indexed[j].index
	})

	h := taskHeap{}
	heap.Init(&h)
	i := 0
	n := len(tasks)
	time := 0
	order := []int{}

	for i < n || len(h) > 0 {
		if i < n && len(h) == 0 {
			time = max(time, indexed[i].enqueue)
		}
		for i < n && indexed[i].enqueue <= time {
			heap.Push(&h, indexed[i])
			i++
		}
		task := heap.Pop(&h).(taskInfo)
		time += task.duration
		order = append(order, task.index)
	}
	return order
}
