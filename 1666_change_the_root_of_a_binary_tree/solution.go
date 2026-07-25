// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Parent *Node
}

func flipBinaryTree(root, leaf *Node) *Node {
	node := leaf
	for node != root {
		parent := node.Parent
		if parent.Left == node {
			parent.Left = nil
		} else {
			parent.Right = nil
		}
		originalLeft := node.Left
		node.Left = parent
		if originalLeft != nil {
			node.Right = originalLeft
		}
		node = parent
	}
	var fixParent func(cur, parent *Node)
	fixParent = func(cur, parent *Node) {
		if cur == nil {
			return
		}
		cur.Parent = parent
		fixParent(cur.Left, cur)
		fixParent(cur.Right, cur)
	}
	fixParent(leaf, nil)
	return leaf
}
