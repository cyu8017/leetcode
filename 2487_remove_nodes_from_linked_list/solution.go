// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNodes(head *ListNode) *ListNode {
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
	mx := 0
	dummy := &ListNode{Next: head}
	prev := dummy
	for prev.Next != nil {
		if prev.Next.Val >= mx {
			mx = prev.Next.Val
			prev = prev.Next
		} else {
			prev.Next = prev.Next.Next
		}
	}
	return rev(dummy.Next)
}
