// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findLeaves(root *TreeNode) [][]int {
	layers := make([][]int, 0)

	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return -1
		}

		height := max(dfs(node.Left), dfs(node.Right)) + 1
		for len(layers) <= height {
			layers = append(layers, make([]int, 0))
		}
		layers[height] = append(layers[height], node.Val)
		return height
	}

	dfs(root)
	return layers
}
