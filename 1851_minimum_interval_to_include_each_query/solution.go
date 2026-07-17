// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

import (
	"container/heap"
	"sort"
)

type intervalHeapItem struct {
	length int
	right  int
}

type intervalHeap []intervalHeapItem

func (values intervalHeap) Len() int           { return len(values) }
func (values intervalHeap) Less(i, j int) bool { return values[i].length < values[j].length }
func (values intervalHeap) Swap(i, j int)      { values[i], values[j] = values[j], values[i] }
func (values *intervalHeap) Push(value interface{}) {
	*values = append(*values, value.(intervalHeapItem))
}
func (values *intervalHeap) Pop() interface{} {
	old := *values
	item := old[len(old)-1]
	*values = old[:len(old)-1]
	return item
}

func minInterval(intervals [][]int, queries []int) []int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	type queryItem struct {
		index int
		value int
	}
	indexedQueries := make([]queryItem, len(queries))
	for index, query := range queries {
		indexedQueries[index] = queryItem{index, query}
	}
	sort.Slice(indexedQueries, func(i, j int) bool {
		return indexedQueries[i].value < indexedQueries[j].value
	})

	answer := make([]int, len(queries))
	for index := range answer {
		answer[index] = -1
	}

	active := &intervalHeap{}
	heap.Init(active)
	intervalIndex := 0

	for _, item := range indexedQueries {
		query := item.value
		for intervalIndex < len(intervals) && intervals[intervalIndex][0] <= query {
			left, right := intervals[intervalIndex][0], intervals[intervalIndex][1]
			heap.Push(active, intervalHeapItem{right - left + 1, right})
			intervalIndex++
		}
		for active.Len() > 0 && (*active)[0].right < query {
			heap.Pop(active)
		}
		if active.Len() > 0 {
			answer[item.index] = (*active)[0].length
		}
	}

	return answer
}
