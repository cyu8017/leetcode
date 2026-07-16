// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderSuccessor(root, p *TreeNode) *TreeNode {
	if p.Right != nil {
		current := p.Right
		for current.Left != nil {
			current = current.Left
		}
		return current
	}

	var successor *TreeNode
	current := root
	for current != nil {
		if p.Val < current.Val {
			successor = current
			current = current.Left
		} else {
			current = current.Right
		}
	}
	return successor
}
