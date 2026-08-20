// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countGreatEnoughNodes(root *TreeNode, k int) int {
	ans := 0
	var dfs func(*TreeNode) []int
	dfs = func(node *TreeNode) []int {
		if node == nil {
			return nil
		}
		vals := []int{node.Val}
		vals = append(vals, dfs(node.Left)...)
		vals = append(vals, dfs(node.Right)...)
		sort.Ints(vals)
		if len(vals) >= k && node.Val > vals[k-1] {
			// great enough: at least k nodes in subtree strictly smaller
		}
		smaller := 0
		for _, v := range vals {
			if v < node.Val {
				smaller++
			}
		}
		if smaller >= k {
			ans++
		}
		return vals
	}
	dfs(root)
	return ans
}
