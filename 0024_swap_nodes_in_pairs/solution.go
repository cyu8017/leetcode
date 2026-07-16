// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	previous := dummy

	for previous.Next != nil && previous.Next.Next != nil {
		first := previous.Next
		second := previous.Next.Next
		first.Next = second.Next
		second.Next = first
		previous.Next = second
		previous = first
	}
	return dummy.Next
}
