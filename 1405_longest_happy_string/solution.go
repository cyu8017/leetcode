// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

import "container/heap"

type item struct {
	count int
	char  byte
}
type maxHeap []item

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].count > h[j].count }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func longestDiverseString(a int, b int, c int) string {
	h := &maxHeap{}
	heap.Init(h)
	for _, p := range []item{{a, 'a'}, {b, 'b'}, {c, 'c'}} {
		if p.count > 0 {
			heap.Push(h, p)
		}
	}
	answer := []byte{}
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		n := len(answer)
		if n >= 2 && answer[n-1] == cur.char && answer[n-2] == cur.char {
			if h.Len() == 0 {
				break
			}
			cur2 := heap.Pop(h).(item)
			answer = append(answer, cur2.char)
			if cur2.count-1 > 0 {
				heap.Push(h, item{cur2.count - 1, cur2.char})
			}
			heap.Push(h, cur)
		} else {
			answer = append(answer, cur.char)
			if cur.count-1 > 0 {
				heap.Push(h, item{cur.count - 1, cur.char})
			}
		}
	}
	return string(answer)
}
