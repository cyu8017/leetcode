// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countUnivalSubtrees(root *TreeNode) int {
	count := 0

	var dfs func(node *TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		leftOk := dfs(node.Left)
		rightOk := dfs(node.Right)
		if !leftOk || !rightOk {
			return false
		}
		if node.Left != nil && node.Left.Val != node.Val {
			return false
		}
		if node.Right != nil && node.Right.Val != node.Val {
			return false
		}
		count++
		return true
	}

	dfs(root)
	return count
}
