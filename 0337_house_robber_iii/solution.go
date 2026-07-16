// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rob(root *TreeNode) int {
	var dfs func(node *TreeNode) (withRob int, withoutRob int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}

		leftWith, leftWithout := dfs(node.Left)
		rightWith, rightWithout := dfs(node.Right)

		withRob := node.Val + leftWithout + rightWithout
		withoutRob := max(leftWith, leftWithout) + max(rightWith, rightWithout)
		return withRob, withoutRob
	}

	withRob, withoutRob := dfs(root)
	return max(withRob, withoutRob)
}
