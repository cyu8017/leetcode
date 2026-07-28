// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverFromPreorder(traversal string) *TreeNode {
	stack := []*TreeNode{}
	i, n := 0, len(traversal)
	for i < n {
		depth := 0
		for i < n && traversal[i] == '-' {
			depth++
			i++
		}
		start := i
		for i < n && traversal[i] >= '0' && traversal[i] <= '9' {
			i++
		}
		val := 0
		for k := start; k < i; k++ {
			val = val*10 + int(traversal[k]-'0')
		}
		node := &TreeNode{Val: val}
		for len(stack) > depth {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > 0 {
			if stack[len(stack)-1].Left == nil {
				stack[len(stack)-1].Left = node
			} else {
				stack[len(stack)-1].Right = node
			}
		}
		stack = append(stack, node)
	}
	return stack[0]
}
