// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/


type ListNode struct {
	Val  int
	Next *ListNode
}

func splitCircularLinkedList(list *ListNode) []*ListNode {
	if list == nil {
		return []*ListNode{nil, nil}
	}
	slow, fast := list, list
	for fast.Next != list && fast.Next.Next != list {
		slow = slow.Next
		fast = fast.Next.Next
	}
	if fast.Next.Next == list {
		fast = fast.Next
	}
	head2 := slow.Next
	slow.Next = list
	fast.Next = head2
	return []*ListNode{list, head2}
}
