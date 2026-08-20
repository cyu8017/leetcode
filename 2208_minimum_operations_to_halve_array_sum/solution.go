// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

import "container/heap"

type maxF2208 []float64

func (h maxF2208) Len() int            { return len(h) }
func (h maxF2208) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxF2208) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxF2208) Push(x interface{}) { *h = append(*h, x.(float64)) }
func (h *maxF2208) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func halveArray(nums []int) int {
	h := &maxF2208{}
	var sum float64
	for _, x := range nums {
		heap.Push(h, float64(x))
		sum += float64(x)
	}
	target := sum / 2
	ans := 0
	for sum > target {
		x := heap.Pop(h).(float64) / 2
		sum -= x
		heap.Push(h, x)
		ans++
	}
	return ans
}
