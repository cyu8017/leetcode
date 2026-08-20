// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestUnivaluePath(root *TreeNode) int {
	best := 0
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		leftPath, rightPath := 0, 0
		if node.Left != nil && node.Left.Val == node.Val {
			leftPath = left + 1
		}
		if node.Right != nil && node.Right.Val == node.Val {
			rightPath = right + 1
		}
		if leftPath+rightPath > best {
			best = leftPath + rightPath
		}
		if leftPath > rightPath {
			return leftPath
		}
		return rightPath
	}
	dfs(root)
	return best
}
