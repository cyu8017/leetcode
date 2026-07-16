// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

import "strconv"
import "strings"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {
	result := []string{}

	var dfs func(node *TreeNode, path []string)
	dfs = func(node *TreeNode, path []string) {
		if node == nil {
			return
		}
		path = append(path, strconv.Itoa(node.Val))
		if node.Left == nil && node.Right == nil {
			result = append(result, strings.Join(path, "->"))
			return
		}
		dfs(node.Left, path)
		dfs(node.Right, path)
	}

	dfs(root, nil)
	return result
}
