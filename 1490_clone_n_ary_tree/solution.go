// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

type Node struct {
	Val      int
	Children []*Node
}

func cloneTree(root *Node) *Node {
	if root == nil {
		return nil
	}
	children := make([]*Node, len(root.Children))
	for i, child := range root.Children {
		children[i] = cloneTree(child)
	}
	return &Node{Val: root.Val, Children: children}
}
