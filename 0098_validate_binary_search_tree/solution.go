// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	var valid func(node *TreeNode, low, high int64) bool
	valid = func(node *TreeNode, low, high int64) bool {
		if node == nil {
			return true
		}
		val := int64(node.Val)
		if !(low < val && val < high) {
			return false
		}
		return valid(node.Left, low, val) && valid(node.Right, val, high)
	}
	return valid(root, math.MinInt64, math.MaxInt64)
}
