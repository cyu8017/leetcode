// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubPath(head *ListNode, root *TreeNode) bool {
	var match func(*ListNode, *TreeNode) bool
	match = func(a *ListNode, b *TreeNode) bool {
		if a == nil {
			return true
		}
		if b == nil || a.Val != b.Val {
			return false
		}
		return match(a.Next, b.Left) || match(a.Next, b.Right)
	}
	if root == nil {
		return false
	}
	return match(head, root) || isSubPath(head, root.Left) || isSubPath(head, root.Right)
}
