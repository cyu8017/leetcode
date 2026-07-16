// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mirrors(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil || left.Val != right.Val {
		return false
	}
	return mirrors(left.Left, right.Right) && mirrors(left.Right, right.Left)
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return mirrors(root.Left, root.Right)
}
