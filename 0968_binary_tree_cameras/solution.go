// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minCameraCover(root *TreeNode) int {
	cameras := 0
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 1
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		if left == 0 || right == 0 {
			cameras++
			return 2
		}
		if left == 2 || right == 2 {
			return 1
		}
		return 0
	}
	rootState := dfs(root)
	if rootState == 0 {
		return cameras + 1
	}
	return cameras
}
