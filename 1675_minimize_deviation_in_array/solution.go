// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

import "container/heap"

type maxHeap1675 []int

func (h maxHeap1675) Len() int            { return len(h) }
func (h maxHeap1675) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap1675) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap1675) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap1675) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumDeviation(nums []int) int {
	h := maxHeap1675{}
	mn := int(1e18)
	for _, x := range nums {
		if x%2 == 1 {
			x *= 2
		}
		if x < mn {
			mn = x
		}
		heap.Push(&h, x)
	}
	ans := int(1e18)
	for {
		x := heap.Pop(&h).(int)
		if x-mn < ans {
			ans = x - mn
		}
		if x%2 == 1 {
			return ans
		}
		x /= 2
		if x < mn {
			mn = x
		}
		heap.Push(&h, x)
	}
}
