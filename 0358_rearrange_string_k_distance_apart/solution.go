// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

import (
	"container/heap"
	"strings"
)

type charCount struct {
	ch    byte
	count int
}

type maxHeap []charCount

func (h maxHeap) Len() int { return len(h) }

func (h maxHeap) Less(i, j int) bool {
	if h[i].count != h[j].count {
		return h[i].count > h[j].count
	}
	return h[i].ch < h[j].ch
}

func (h maxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(charCount))
}

func (h *maxHeap) Pop() interface{} {
	item := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return item
}

type queueItem struct {
	count    int
	ch       byte
	readyAt  int
}

func rearrangeString(s string, k int) string {
	counts := make(map[byte]int)
	for index := 0; index < len(s); index++ {
		counts[s[index]]++
	}

	maxFreq := 0
	for _, count := range counts {
		if count > maxFreq {
			maxFreq = count
		}
	}

	maxFreqChars := 0
	for _, count := range counts {
		if count == maxFreq {
			maxFreqChars++
		}
	}

	if (len(s)-maxFreqChars) < (maxFreq-1)*(k-1) {
		return ""
	}

	h := &maxHeap{}
	heap.Init(h)
	for ch, count := range counts {
		heap.Push(h, charCount{ch: ch, count: count})
	}

	queue := make([]queueItem, 0)
	var builder strings.Builder
	index := 0

	for h.Len() > 0 || len(queue) > 0 {
		for len(queue) > 0 && queue[0].readyAt <= index {
			item := queue[0]
			queue = queue[1:]
			heap.Push(h, charCount{ch: item.ch, count: item.count})
		}

		if h.Len() == 0 {
			return ""
		}

		top := heap.Pop(h).(charCount)
		builder.WriteByte(top.ch)
		if top.count-1 > 0 {
			queue = append(queue, queueItem{
				count:   top.count - 1,
				ch:      top.ch,
				readyAt: index + k,
			})
		}
		index++
	}

	return builder.String()
}
