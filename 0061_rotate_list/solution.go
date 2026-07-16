// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	tail := head
	length := 1
	for tail.Next != nil {
		tail = tail.Next
		length++
	}

	tail.Next = head
	k %= length
	if k == 0 {
		tail.Next = nil
		return head
	}

	steps := length - k
	newTail := head
	for i := 0; i < steps-1; i++ {
		newTail = newTail.Next
	}

	newHead := newTail.Next
	newTail.Next = nil
	return newHead
}
