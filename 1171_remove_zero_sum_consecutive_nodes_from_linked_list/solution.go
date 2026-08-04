// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeZeroSumSublists(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	prefix := 0
	seen := map[int]*ListNode{0: dummy}
	for node := dummy; node != nil; node = node.Next {
		prefix += node.Val
		seen[prefix] = node
	}
	prefix = 0
	for node := dummy; node != nil; node = node.Next {
		prefix += node.Val
		node.Next = seen[prefix].Next
	}
	return dummy.Next
}
