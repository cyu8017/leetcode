// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

type Node struct {
	Val      int
	Children []*Node
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func encodeNaryTree(root *Node) *TreeNode {
	if root == nil {
		return nil
	}

	binary := &TreeNode{Val: root.Val}
	if len(root.Children) == 0 {
		return binary
	}

	binary.Left = encodeNaryTree(root.Children[0])
	sibling := binary.Left
	for index := 1; index < len(root.Children); index++ {
		sibling.Right = encodeNaryTree(root.Children[index])
		sibling = sibling.Right
	}
	return binary
}

func decodeBinaryTree(root *TreeNode) *Node {
	if root == nil {
		return nil
	}

	node := &Node{Val: root.Val, Children: make([]*Node, 0)}
	for current := root.Left; current != nil; current = current.Right {
		node.Children = append(node.Children, decodeBinaryTree(current))
	}
	return node
}
