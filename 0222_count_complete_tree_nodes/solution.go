// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leftDepth(node *TreeNode) int {
	depth := 0
	for node != nil {
		depth++
		node = node.Left
	}
	return depth
}

func rightDepth(node *TreeNode) int {
	depth := 0
	for node != nil {
		depth++
		node = node.Right
	}
	return depth
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := leftDepth(root)
	right := rightDepth(root)
	if left == right {
		return (1 << left) - 1
	}
	return 1 + countNodes(root.Left) + countNodes(root.Right)
}
