// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/


import "container/heap"

type maxH []int
func (h maxH) Len() int            { return len(h) }
func (h maxH) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxH) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxH) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func pickGifts(gifts []int, k int) int64 {
	h := maxH(append([]int(nil), gifts...))
	heap.Init(&h)
	for i := 0; i < k; i++ {
		x := heap.Pop(&h).(int)
		// integer square root
		lo, hi := 0, x
		for lo < hi {
			mid := (lo + hi + 1) / 2
			if mid*mid <= x {
				lo = mid
			} else {
				hi = mid - 1
			}
		}
		heap.Push(&h, lo)
	}
	var ans int64
	for _, v := range h {
		ans += int64(v)
	}
	return ans
}
