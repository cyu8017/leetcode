// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findTilt(root *TreeNode) int {
	total := 0
	var subtreeSum func(node *TreeNode) int
	subtreeSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := subtreeSum(node.Left)
		right := subtreeSum(node.Right)
		diff := left - right
		if diff < 0 {
			diff = -diff
		}
		total += diff
		return node.Val + left + right
	}
	subtreeSum(root)
	return total
}
