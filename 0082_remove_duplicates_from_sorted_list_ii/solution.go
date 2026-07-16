// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	previous := dummy

	for head != nil {
		if head.Next != nil && head.Val == head.Next.Val {
			for head.Next != nil && head.Val == head.Next.Val {
				head = head.Next
			}
			previous.Next = head.Next
		} else {
			previous = previous.Next
		}
		head = head.Next
	}

	return dummy.Next
}
