// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	best := 0
	var depth func(node *TreeNode) int
	depth = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := depth(node.Left)
		right := depth(node.Right)
		if left+right > best {
			best = left + right
		}
		if left > right {
			return 1 + left
		}
		return 1 + right
	}
	depth(root)
	return best
}
