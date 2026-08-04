// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

import "container/heap"

type item struct{ value, i, j int }
type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].value < h[j].value }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthSmallest(mat [][]int, k int) int {
	sums := []int{0}
	for _, row := range mat {
		h := &minHeap{{sums[0] + row[0], 0, 0}}
		heap.Init(h)
		merged := []int{}
		for h.Len() > 0 && len(merged) < k {
			cur := heap.Pop(h).(item)
			merged = append(merged, cur.value)
			if cur.j+1 < len(row) {
				heap.Push(h, item{sums[cur.i] + row[cur.j+1], cur.i, cur.j + 1})
			}
			if cur.j == 0 && cur.i+1 < len(sums) {
				heap.Push(h, item{sums[cur.i+1] + row[0], cur.i + 1, 0})
			}
		}
		sums = merged
	}
	return sums[k-1]
}
