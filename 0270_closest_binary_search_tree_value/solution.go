// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func closestValue(root *TreeNode, target float64) int {
	closest := root.Val
	current := root
	for current != nil {
		if math.Abs(float64(closest)-target) > math.Abs(float64(current.Val)-target) {
			closest = current.Val
		}
		if float64(current.Val) == target {
			return current.Val
		}
		if target < float64(current.Val) {
			current = current.Left
		} else {
			current = current.Right
		}
	}
	return closest
}
