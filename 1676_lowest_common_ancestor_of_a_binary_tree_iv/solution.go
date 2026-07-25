// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root *TreeNode, nodes []*TreeNode) *TreeNode {
	targets := make(map[*TreeNode]bool, len(nodes))
	for _, n := range nodes {
		targets[n] = true
	}
	var dfs func(node *TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		l := dfs(node.Left)
		r := dfs(node.Right)
		if targets[node] || (l != nil && r != nil) {
			return node
		}
		if l != nil {
			return l
		}
		return r
	}
	return dfs(root)
}
