// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

import "container/heap"

type GridMaster interface {
	CanMove(direction string) bool
	Move(direction string) int
	IsTarget() bool
}

type pathItem struct {
	dist int
	r    int
	c    int
}

type pathHeap []pathItem

func (h pathHeap) Len() int            { return len(h) }
func (h pathHeap) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h pathHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pathHeap) Push(x interface{}) { *h = append(*h, x.(pathItem)) }
func (h *pathHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

func findShortestPath(master GridMaster) int {
	dirs := map[string][2]int{
		"U": {-1, 0},
		"D": {1, 0},
		"L": {0, -1},
		"R": {0, 1},
	}
	opp := map[string]string{
		"U": "D",
		"D": "U",
		"L": "R",
		"R": "L",
	}

	moveCost := map[[2]int]int{{0, 0}: 0}
	var target *[2]int

	if master.IsTarget() {
		return 0
	}

	var dfs func(r, c int)
	dfs = func(r, c int) {
		for direction, delta := range dirs {
			if !master.CanMove(direction) {
				continue
			}
			cost := master.Move(direction)
			nr, nc := r+delta[0], c+delta[1]
			key := [2]int{nr, nc}
			if _, ok := moveCost[key]; !ok {
				moveCost[key] = cost
				if master.IsTarget() {
					t := key
					target = &t
				}
				dfs(nr, nc)
			}
			master.Move(opp[direction])
		}
	}
	dfs(0, 0)

	if target == nil {
		return -1
	}

	heapImpl := pathHeap{{dist: 0, r: 0, c: 0}}
	best := map[[2]int]int{{0, 0}: 0}
	heap.Init(&heapImpl)

	for heapImpl.Len() > 0 {
		item := heap.Pop(&heapImpl).(pathItem)
		if item.r == target[0] && item.c == target[1] {
			return item.dist
		}
		key := [2]int{item.r, item.c}
		if item.dist > best[key] {
			continue
		}
		for _, delta := range dirs {
			nr, nc := item.r+delta[0], item.c+delta[1]
			nextKey := [2]int{nr, nc}
			cost, ok := moveCost[nextKey]
			if !ok {
				continue
			}
			nd := item.dist + cost
			if prev, exists := best[nextKey]; !exists || nd < prev {
				best[nextKey] = nd
				heap.Push(&heapImpl, pathItem{dist: nd, r: nr, c: nc})
			}
		}
	}
	return -1
}
