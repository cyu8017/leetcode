// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func correctBinaryTree(root *TreeNode) *TreeNode {
	seen := map[*TreeNode]bool{}
	var dfs func(node *TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		if seen[node.Right] {
			return nil
		}
		seen[node] = true
		node.Right = dfs(node.Right)
		node.Left = dfs(node.Left)
		return node
	}
	return dfs(root)
}
