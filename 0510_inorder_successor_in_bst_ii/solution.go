// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Parent *Node
}

func inorderSuccessor(node *Node) *Node {
	if node.Right != nil {
		current := node.Right
		for current.Left != nil {
			current = current.Left
		}
		return current
	}

	current := node
	for current.Parent != nil && current == current.Parent.Right {
		current = current.Parent
	}
	return current.Parent
}
