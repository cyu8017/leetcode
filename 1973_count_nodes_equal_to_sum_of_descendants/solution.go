// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func equalToDescendants(root *TreeNode) int {
	ans := 0
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		total := dfs(node.Left) + dfs(node.Right)
		if total == node.Val {
			ans++
		}
		return total + node.Val
	}
	dfs(root)
	return ans
}
