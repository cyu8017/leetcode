// LeetCode 0111 - Minimum Depth of Binary Tree
type TreeNode struct { Val int; Left, Right *TreeNode }
func minDepth(root *TreeNode) int {
	if root == nil { return 0 }
	if root.Left == nil { return 1 + minDepth(root.Right) }
	if root.Right == nil { return 1 + minDepth(root.Left) }
	a, b := minDepth(root.Left), minDepth(root.Right)
	if a < b { return a + 1 }; return b + 1
}