// LeetCode 0404 - Sum of Left Leaves
// https://leetcode.com/problems/sum-of-left-leaves/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}

	total := 0
	if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
		total += root.Left.Val
	} else {
		total += sumOfLeftLeaves(root.Left)
	}

	total += sumOfLeftLeaves(root.Right)
	return total
}
