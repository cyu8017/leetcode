// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

import "container/heap"

type busyItem struct {
	end, server int
}

type busyHeap []busyItem

func (h busyHeap) Len() int            { return len(h) }
func (h busyHeap) Less(i, j int) bool  { return h[i].end < h[j].end }
func (h busyHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *busyHeap) Push(x interface{}) { *h = append(*h, x.(busyItem)) }
func (h *busyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type freeHeap []int

func (h freeHeap) Len() int            { return len(h) }
func (h freeHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h freeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *freeHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *freeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func busiestServers(k int, arrival []int, load []int) []int {
	free := freeHeap{}
	for i := 0; i < k; i++ {
		heap.Push(&free, i)
	}
	busy := busyHeap{}
	count := make([]int, k)
	for i, t := range arrival {
		for busy.Len() > 0 && busy[0].end <= t {
			item := heap.Pop(&busy).(busyItem)
			heap.Push(&free, i+(item.server-i)%k)
		}
		if free.Len() == 0 {
			continue
		}
		server := heap.Pop(&free).(int) % k
		count[server]++
		heap.Push(&busy, busyItem{end: t + load[i], server: server})
	}
	best := 0
	for _, c := range count {
		if c > best {
			best = c
		}
	}
	ans := []int{}
	for i, c := range count {
		if c == best {
			ans = append(ans, i)
		}
	}
	return ans
}
