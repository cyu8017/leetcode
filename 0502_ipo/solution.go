// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

import (
	"container/heap"
	"sort"
)

type project struct {
	capital int
	profit  int
}

type profitHeap []int

func (values profitHeap) Len() int            { return len(values) }
func (values profitHeap) Less(i, j int) bool  { return values[i] > values[j] }
func (values profitHeap) Swap(i, j int)       { values[i], values[j] = values[j], values[i] }
func (values *profitHeap) Push(value interface{}) {
	*values = append(*values, value.(int))
}
func (values *profitHeap) Pop() interface{} {
	old := *values
	item := old[len(old)-1]
	*values = old[:len(old)-1]
	return item
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	projects := make([]project, len(capital))
	for index := range capital {
		projects[index] = project{capital: capital[index], profit: profits[index]}
	}
	sort.Slice(projects, func(i, j int) bool {
		return projects[i].capital < projects[j].capital
	})

	available := &profitHeap{}
	heap.Init(available)
	index := 0
	for round := 0; round < k; round++ {
		for index < len(projects) && projects[index].capital <= w {
			heap.Push(available, projects[index].profit)
			index++
		}
		if available.Len() == 0 {
			break
		}
		w += heap.Pop(available).(int)
	}
	return w
}
