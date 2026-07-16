// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

import "container/heap"

type ListNode struct {
	Val  int
	Next *ListNode
}

type heapNode struct {
	val    int
	index  int
	node   *ListNode
}

type nodeHeap []*heapNode

func (h nodeHeap) Len() int            { return len(h) }
func (h nodeHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h nodeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *nodeHeap) Push(x interface{}) { *h = append(*h, x.(*heapNode)) }
func (h *nodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func mergeKLists(lists []*ListNode) *ListNode {
	h := &nodeHeap{}
	heap.Init(h)
	for i, node := range lists {
		if node != nil {
			heap.Push(h, &heapNode{val: node.Val, index: i, node: node})
		}
	}

	dummy := &ListNode{}
	current := dummy
	for h.Len() > 0 {
		item := heap.Pop(h).(*heapNode)
		current.Next = item.node
		current = current.Next
		if item.node.Next != nil {
			heap.Push(h, &heapNode{val: item.node.Next.Val, index: item.index, node: item.node.Next})
		}
	}
	return dummy.Next
}
