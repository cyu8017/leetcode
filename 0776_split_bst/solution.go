// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func splitBST(root *TreeNode, target int) []*TreeNode {
	if root == nil {
		return []*TreeNode{nil, nil}
	}
	if root.Val <= target {
		parts := splitBST(root.Right, target)
		root.Right = parts[0]
		return []*TreeNode{root, parts[1]}
	}
	parts := splitBST(root.Left, target)
	root.Left = parts[1]
	return []*TreeNode{parts[0], root}
}
