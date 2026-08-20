// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func heightOfTree(root *TreeNode) int {
	if root == nil {
		return -1
	}
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return -1
		}
		if node.Left != nil && node.Left.Right == node {
			return dfs(node.Right) + 1
		}
		if node.Right != nil && node.Right.Left == node {
			return dfs(node.Left) + 1
		}
		return max(dfs(node.Left), dfs(node.Right)) + 1
	}
	return dfs(root)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
