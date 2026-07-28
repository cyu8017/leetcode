// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxAncestorDiff(root *TreeNode) int {
	var dfs func(node *TreeNode, lo, hi int) int
	dfs = func(node *TreeNode, lo, hi int) int {
		if node == nil {
			return hi - lo
		}
		if node.Val < lo {
			lo = node.Val
		}
		if node.Val > hi {
			hi = node.Val
		}
		left := dfs(node.Left, lo, hi)
		right := dfs(node.Right, lo, hi)
		if left > right {
			return left
		}
		return right
	}
	return dfs(root, root.Val, root.Val)
}
