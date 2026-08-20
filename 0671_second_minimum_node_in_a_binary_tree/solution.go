// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findSecondMinimumValue(root *TreeNode) int {
	if root == nil {
		return -1
	}
	ans := -1
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		if node.Val > root.Val {
			if ans == -1 || node.Val < ans {
				ans = node.Val
			}
			return
		}
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return ans
}
