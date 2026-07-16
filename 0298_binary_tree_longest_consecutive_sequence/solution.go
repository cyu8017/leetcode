// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestConsecutive(root *TreeNode) int {
	var dfs func(node, parent *TreeNode, length int) int
	dfs = func(node, parent *TreeNode, length int) int {
		if node == nil {
			return 0
		}

		current := 1
		if parent != nil && parent.Val+1 == node.Val {
			current = length + 1
		}
		left := dfs(node.Left, node, current)
		right := dfs(node.Right, node, current)
		if left > current {
			current = left
		}
		if right > current {
			current = right
		}
		return current
	}

	return dfs(root, nil, 0)
}
