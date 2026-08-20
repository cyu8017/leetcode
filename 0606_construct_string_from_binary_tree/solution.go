// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func tree2str(root *TreeNode) string {
	if root == nil {
		return ""
	}
	result := strconv.Itoa(root.Val)
	if root.Left != nil || root.Right != nil {
		result += "(" + tree2str(root.Left) + ")"
	}
	if root.Right != nil {
		result += "(" + tree2str(root.Right) + ")"
	}
	return result
}
