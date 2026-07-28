// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sufficientSubset(root *TreeNode, limit int) *TreeNode {
	var dfs func(node *TreeNode, pathSum int) *TreeNode
	dfs = func(node *TreeNode, pathSum int) *TreeNode {
		if node == nil {
			return nil
		}
		pathSum += node.Val
		if node.Left == nil && node.Right == nil {
			if pathSum >= limit {
				return node
			}
			return nil
		}
		node.Left = dfs(node.Left, pathSum)
		node.Right = dfs(node.Right, pathSum)
		if node.Left == nil && node.Right == nil {
			return nil
		}
		return node
	}
	return dfs(root, 0)
}
