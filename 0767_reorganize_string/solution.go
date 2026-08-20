// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

import "container/heap"

type charCount struct {
	count int
	ch    byte
}
type maxHeap []charCount

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].count > h[j].count }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(charCount)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func reorganizeString(s string) string {
	freq := map[byte]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]]++
	}
	h := &maxHeap{}
	heap.Init(h)
	for ch, count := range freq {
		heap.Push(h, charCount{count, ch})
	}
	if (*h)[0].count > (len(s)+1)/2 {
		return ""
	}
	result := make([]byte, 0, len(s))
	for h.Len() >= 2 {
		a := heap.Pop(h).(charCount)
		b := heap.Pop(h).(charCount)
		result = append(result, a.ch, b.ch)
		if a.count-1 > 0 {
			heap.Push(h, charCount{a.count - 1, a.ch})
		}
		if b.count-1 > 0 {
			heap.Push(h, charCount{b.count - 1, b.ch})
		}
	}
	if h.Len() > 0 {
		result = append(result, (*h)[0].ch)
	}
	return string(result)
}
