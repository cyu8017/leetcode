// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

type ListNode struct {
	Val  int
	Next *ListNode
}

func sortLinkedList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	prev, cur := head, head.Next
	for cur != nil {
		if cur.Val < 0 {
			prev.Next = cur.Next
			cur.Next = head
			head = cur
			cur = prev.Next
		} else {
			prev = cur
			cur = cur.Next
		}
	}
	return head
}
