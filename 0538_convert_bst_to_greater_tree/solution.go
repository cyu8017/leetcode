// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func convertBST(root *TreeNode) {
	running := 0
	var reverseInorder func(node *TreeNode)
	reverseInorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		reverseInorder(node.Right)
		running += node.Val
		node.Val = running
		reverseInorder(node.Left)
	}
	reverseInorder(root)
}
