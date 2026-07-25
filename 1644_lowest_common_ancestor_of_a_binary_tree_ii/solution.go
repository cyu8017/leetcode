// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	found := 0
	var dfs func(*TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		if node == p || node == q {
			found++
			return node
		}
		if left != nil && right != nil {
			return node
		}
		if left != nil {
			return left
		}
		return right
	}
	ans := dfs(root)
	if found == 2 {
		return ans
	}
	return nil
}
