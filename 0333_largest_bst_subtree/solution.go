// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestBSTSubtree(root *TreeNode) int {
	best := 0

	var dfs func(node *TreeNode) (bool, int, int, int)
	dfs = func(node *TreeNode) (bool, int, int, int) {
		if node == nil {
			return true, math.MaxInt32, math.MinInt32, 0
		}

		leftOk, leftMin, leftMax, leftSize := dfs(node.Left)
		rightOk, rightMin, rightMax, rightSize := dfs(node.Right)

		if leftOk && rightOk && leftMax < node.Val && node.Val < rightMin {
			size := leftSize + rightSize + 1
			if size > best {
				best = size
			}
			minValue := node.Val
			if leftMin < minValue {
				minValue = leftMin
			}
			maxValue := node.Val
			if rightMax > maxValue {
				maxValue = rightMax
			}
			return true, minValue, maxValue, size
		}

		return false, 0, 0, 0
	}

	dfs(root)
	return best
}
