// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

import "container/heap"

type loc2102 struct {
	name  string
	score int
}

type minH2102 []loc2102
type maxH2102 []loc2102

func (h minH2102) Len() int { return len(h) }
func (h minH2102) Less(i, j int) bool {
	if h[i].score != h[j].score {
		return h[i].score < h[j].score
	}
	return h[i].name > h[j].name
}
func (h minH2102) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH2102) Push(x interface{}) { *h = append(*h, x.(loc2102)) }
func (h *minH2102) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func (h maxH2102) Len() int { return len(h) }
func (h maxH2102) Less(i, j int) bool {
	if h[i].score != h[j].score {
		return h[i].score > h[j].score
	}
	return h[i].name < h[j].name
}
func (h maxH2102) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxH2102) Push(x interface{}) { *h = append(*h, x.(loc2102)) }
func (h *maxH2102) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

type SORTracker struct {
	best minH2102
	rest maxH2102
	k    int
}

func Constructor() SORTracker {
	return SORTracker{}
}

func (this *SORTracker) Add(name string, score int) {
	item := loc2102{name, score}
	heap.Push(&this.best, item)
	if this.best.Len() > this.k {
		heap.Push(&this.rest, heap.Pop(&this.best).(loc2102))
	}
}

func (this *SORTracker) Get() string {
	this.k++
	if this.rest.Len() > 0 {
		heap.Push(&this.best, heap.Pop(&this.rest).(loc2102))
	}
	return this.best[0].name
}
