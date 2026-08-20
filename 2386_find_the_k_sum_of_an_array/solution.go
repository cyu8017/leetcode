// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

import (
	"container/heap"
	"sort"
)

type pair struct {
	sum int64
	i   int
}

type PQ []pair

func (h PQ) Len() int            { return len(h) }
func (h PQ) Less(i, j int) bool  { return h[i].sum > h[j].sum }
func (h PQ) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *PQ) Push(x interface{}) { *h = append(*h, x.(pair)) }
func (h *PQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kSum(nums []int, k int) int64 {
	var total int64
	absNums := make([]int, len(nums))
	for i, x := range nums {
		if x >= 0 {
			total += int64(x)
			absNums[i] = x
		} else {
			absNums[i] = -x
		}
	}
	sort.Ints(absNums)
	h := &PQ{{total, 0}}
	heap.Init(h)
	for t := 0; t < k-1; t++ {
		cur := heap.Pop(h).(pair)
		if cur.i >= len(absNums) {
			continue
		}
		heap.Push(h, pair{cur.sum - int64(absNums[cur.i]), cur.i + 1})
		if cur.i > 0 {
			heap.Push(h, pair{cur.sum - int64(absNums[cur.i]) + int64(absNums[cur.i-1]), cur.i + 1})
		}
	}
	return (*h)[0].sum
}
