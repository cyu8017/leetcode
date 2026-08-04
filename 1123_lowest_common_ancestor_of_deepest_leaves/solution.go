// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode) (*TreeNode, int)
	dfs = func(node *TreeNode) (*TreeNode, int) {
		if node == nil {
			return nil, 0
		}
		ln, ld := dfs(node.Left)
		rn, rd := dfs(node.Right)
		if ld > rd {
			return ln, ld + 1
		}
		if rd > ld {
			return rn, rd + 1
		}
		return node, ld + 1
	}
	node, _ := dfs(root)
	return node
}
