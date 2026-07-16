// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{Next: head}
	groupPrevious := dummy

	for {
		kth := groupPrevious
		for i := 0; i < k; i++ {
			kth = kth.Next
			if kth == nil {
				return dummy.Next
			}
		}
		groupNext := kth.Next
		previous := groupNext
		current := groupPrevious.Next
		for current != groupNext {
			next := current.Next
			current.Next = previous
			previous = current
			current = next
		}
		tmp := groupPrevious.Next
		groupPrevious.Next = kth
		groupPrevious = tmp
	}
}
