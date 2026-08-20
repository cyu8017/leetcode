// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeNodes(head *ListNode) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	sum := 0
	for p := head.Next; p != nil; p = p.Next {
		if p.Val == 0 {
			cur.Next = &ListNode{Val: sum}
			cur = cur.Next
			sum = 0
		} else {
			sum += p.Val
		}
	}
	return dummy.Next
}
