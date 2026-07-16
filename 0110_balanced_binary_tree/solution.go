// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func height(node *TreeNode) int {
	if node == nil {
		return 0
	}
	left := height(node.Left)
	if left == -1 {
		return -1
	}
	right := height(node.Right)
	if right == -1 {
		return -1
	}
	diff := left - right
	if diff < 0 {
		diff = -diff
	}
	if diff > 1 {
		return -1
	}
	if left > right {
		return 1 + left
	}
	return 1 + right
}

func isBalanced(root *TreeNode) bool {
	return height(root) != -1
}
