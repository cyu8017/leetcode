// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	var first, second, previous *TreeNode
	stack := []*TreeNode{}
	current := root

	for current != nil || len(stack) > 0 {
		for current != nil {
			stack = append(stack, current)
			current = current.Left
		}
		current = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if previous != nil && previous.Val > current.Val {
			if first == nil {
				first = previous
			}
			second = current
		}
		previous = current
		current = current.Right
	}

	if first != nil && second != nil {
		first.Val, second.Val = second.Val, first.Val
	}
}
