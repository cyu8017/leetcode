// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDiffInBST(root *TreeNode) int {
	prev := -1
	best := int(^uint(0) >> 1)
	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if prev != -1 {
			diff := node.Val - prev
			if diff < best {
				best = diff
			}
		}
		prev = node.Val
		inorder(node.Right)
	}
	inorder(root)
	return best
}
