// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || left == right {
		return head
	}

	dummy := &ListNode{Val: 0, Next: head}
	before := dummy
	for i := 0; i < left-1; i++ {
		before = before.Next
	}

	start := before.Next
	current := start.Next

	for i := 0; i < right-left; i++ {
		start.Next = current.Next
		current.Next = before.Next
		before.Next = current
		current = start.Next
	}

	return dummy.Next
}
