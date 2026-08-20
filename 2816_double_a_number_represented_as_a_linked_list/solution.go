// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func doubleIt(head *ListNode) *ListNode {
	var rev func(*ListNode) *ListNode
	rev = func(node *ListNode) *ListNode {
		var prev *ListNode
		for node != nil {
			nxt := node.Next
			node.Next = prev
			prev = node
			node = nxt
		}
		return prev
	}
	head = rev(head)
	carry := 0
	cur := head
	var prev *ListNode
	for cur != nil {
		val := cur.Val*2 + carry
		cur.Val = val % 10
		carry = val / 10
		prev = cur
		cur = cur.Next
	}
	if carry > 0 {
		prev.Next = &ListNode{Val: carry}
	}
	return rev(head)
}
