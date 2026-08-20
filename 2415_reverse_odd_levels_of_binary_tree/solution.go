// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func reverseOddLevels(root *TreeNode) *TreeNode {
	var dfs func(a, b *TreeNode, level int)
	dfs = func(a, b *TreeNode, level int) {
		if a == nil || b == nil {
			return
		}
		if level%2 == 1 {
			a.Val, b.Val = b.Val, a.Val
		}
		dfs(a.Left, b.Right, level+1)
		dfs(a.Right, b.Left, level+1)
	}
	if root != nil {
		dfs(root.Left, root.Right, 1)
	}
	return root
}
