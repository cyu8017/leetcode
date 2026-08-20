// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

import "container/heap"

type minH2233 []int

func (h minH2233) Len() int            { return len(h) }
func (h minH2233) Less(i, j int) bool  { return h[i] < h[j] }
func (h minH2233) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minH2233) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minH2233) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func maximumProduct(nums []int, k int) int {
	const MOD = 1_000_000_007
	h := minH2233(append([]int{}, nums...))
	heap.Init(&h)
	for i := 0; i < k; i++ {
		x := heap.Pop(&h).(int) + 1
		heap.Push(&h, x)
	}
	ans := 1
	for _, x := range h {
		ans = ans * x % MOD
	}
	return ans
}
