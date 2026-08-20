// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

import "container/heap"

type item struct{ cost, idx int }
type PQ []item

func (h PQ) Len() int { return len(h) }
func (h PQ) Less(i, j int) bool {
	if h[i].cost == h[j].cost {
		return h[i].idx < h[j].idx
	}
	return h[i].cost < h[j].cost
}
func (h PQ) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *PQ) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *PQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func totalCost(costs []int, k int, candidates int) int64 {
	n := len(costs)
	leftH, rightH := &PQ{}, &PQ{}
	heap.Init(leftH)
	heap.Init(rightH)
	l, r := 0, n-1
	for l <= r && leftH.Len() < candidates {
		heap.Push(leftH, item{costs[l], l})
		l++
	}
	for r >= l && rightH.Len() < candidates {
		heap.Push(rightH, item{costs[r], r})
		r--
	}
	var ans int64
	for t := 0; t < k; t++ {
		useLeft := false
		if leftH.Len() > 0 && rightH.Len() > 0 {
			if (*leftH)[0].cost < (*rightH)[0].cost || ((*leftH)[0].cost == (*rightH)[0].cost && (*leftH)[0].idx <= (*rightH)[0].idx) {
				useLeft = true
			}
		} else if leftH.Len() > 0 {
			useLeft = true
		}
		if useLeft {
			it := heap.Pop(leftH).(item)
			ans += int64(it.cost)
			if l <= r {
				heap.Push(leftH, item{costs[l], l})
				l++
			}
		} else {
			it := heap.Pop(rightH).(item)
			ans += int64(it.cost)
			if l <= r {
				heap.Push(rightH, item{costs[r], r})
				r--
			}
		}
	}
	return ans
}
