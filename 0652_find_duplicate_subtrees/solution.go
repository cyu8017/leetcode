// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	counts := map[string]int{}
	result := []*TreeNode{}
	var serialize func(node *TreeNode) string
	serialize = func(node *TreeNode) string {
		if node == nil {
			return "#"
		}
		key := fmt.Sprintf("%d,%s,%s", node.Val, serialize(node.Left), serialize(node.Right))
		counts[key]++
		if counts[key] == 2 {
			result = append(result, node)
		}
		return key
	}
	serialize(root)
	return result
}
