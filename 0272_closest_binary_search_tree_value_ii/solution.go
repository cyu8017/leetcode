// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func closestKValues(root *TreeNode, target float64, k int) []int {
	values := make([]int, 0)
	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		values = append(values, node.Val)
		inorder(node.Right)
	}
	inorder(root)

	lo, hi := 0, len(values)
	for lo < hi {
		mid := (lo + hi) / 2
		if float64(values[mid]) < target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	left := lo - 1
	right := lo
	result := make([]int, 0, k)
	for len(result) < k {
		if right >= len(values) ||
			(left >= 0 && math.Abs(float64(values[left])-target) <= math.Abs(float64(values[right])-target)) {
			result = append(result, values[left])
			left--
		} else {
			result = append(result, values[right])
			right++
		}
	}
	return result
}
