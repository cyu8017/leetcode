// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func plusOne(head *ListNode) *ListNode {
	sentinel := &ListNode{Val: 0, Next: head}
	notNine := sentinel
	node := head

	for node != nil {
		if node.Val != 9 {
			notNine = node
		}
		node = node.Next
	}

	notNine.Val++
	node = notNine.Next
	for node != nil {
		node.Val = 0
		node = node.Next
	}

	if sentinel.Val == 1 {
		return sentinel
	}
	return sentinel.Next
}
