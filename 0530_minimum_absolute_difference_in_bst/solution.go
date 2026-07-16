// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMinimumDifference(root *TreeNode) int {
	best := math.MaxInt
	previous := -1
	hasPrevious := false

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if hasPrevious {
			if diff := node.Val - previous; diff < best {
				best = diff
			}
		}
		previous = node.Val
		hasPrevious = true
		inorder(node.Right)
	}

	inorder(root)
	return best
}
