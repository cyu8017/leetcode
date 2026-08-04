// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidSequence(root *TreeNode, arr []int) bool {
	var visit func(*TreeNode, int) bool
	visit = func(node *TreeNode, index int) bool {
		if node == nil || index == len(arr) || node.Val != arr[index] {
			return false
		}
		if node.Left == nil && node.Right == nil {
			return index == len(arr)-1
		}
		return visit(node.Left, index+1) || visit(node.Right, index+1)
	}
	return visit(root, 0)
}
