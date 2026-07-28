// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumRootToLeaf(root *TreeNode) int {
	var dfs func(node *TreeNode, value int) int
	dfs = func(node *TreeNode, value int) int {
		if node == nil {
			return 0
		}
		value = value*2 + node.Val
		if node.Left == nil && node.Right == nil {
			return value
		}
		return dfs(node.Left, value) + dfs(node.Right, value)
	}
	return dfs(root, 0)
}
