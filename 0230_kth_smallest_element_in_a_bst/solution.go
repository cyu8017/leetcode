// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	stack := []*TreeNode{}
	current := root

	for current != nil || len(stack) > 0 {
		for current != nil {
			stack = append(stack, current)
			current = current.Left
		}
		current = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		k--
		if k == 0 {
			return current.Val
		}
		current = current.Right
	}

	return -1
}
