// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	ans := 0
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return -1, -1
		}
		_, lr := dfs(node.Left)
		rl, _ := dfs(node.Right)
		a, b := lr+1, rl+1
		if a > ans {
			ans = a
		}
		if b > ans {
			ans = b
		}
		return a, b
	}
	dfs(root)
	return ans
}
