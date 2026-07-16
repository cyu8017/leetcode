// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func treeToDoublyList(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	var first *TreeNode
	var last *TreeNode

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if last != nil {
			last.Right = node
			node.Left = last
		} else {
			first = node
		}
		last = node
		inorder(node.Right)
	}

	inorder(root)
	if first != nil && last != nil {
		first.Left = last
		last.Right = first
	}
	return first
}
