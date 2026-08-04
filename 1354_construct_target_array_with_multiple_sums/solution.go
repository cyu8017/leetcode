// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

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

func isPossible(target []int) bool {
	if len(target) == 1 {
		return target[0] == 1
	}
	total := 0
	h := &maxHeap{}
	for _, x := range target {
		total += x
		heap.Push(h, x)
	}
	for {
		x := heap.Pop(h).(int)
		rest := total - x
		if x == 1 || rest == 1 {
			return true
		}
		if rest == 0 || x <= rest {
			return false
		}
		prev := x % rest
		if prev == 0 {
			return false
		}
		total = rest + prev
		heap.Push(h, prev)
	}
}
