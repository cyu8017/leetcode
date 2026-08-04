// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNodes(head *ListNode, m int, n int) *ListNode {
	cur := head
	for cur != nil {
		for i := 0; i < m-1; i++ {
			if cur == nil {
				break
			}
			cur = cur.Next
		}
		if cur == nil {
			break
		}
		drop := cur.Next
		for i := 0; i < n; i++ {
			if drop != nil {
				drop = drop.Next
			}
		}
		cur.Next = drop
		cur = drop
	}
	return head
}
