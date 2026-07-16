// LeetCode 0114 - Flatten Binary Tree to Linked List
type TreeNode struct { Val int; Left, Right *TreeNode }
func flatten(root *TreeNode) {
	var prev *TreeNode
	var walk func(*TreeNode)
	walk = func(n *TreeNode) {
		if n == nil { return }; walk(n.Right); walk(n.Left)
		n.Right, n.Left, prev = prev, nil, n
	}
	walk(root)
}