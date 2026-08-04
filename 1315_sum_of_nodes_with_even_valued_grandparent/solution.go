// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumEvenGrandparent(root *TreeNode) int {
	var dfs func(node, parent, grandparent *TreeNode) int
	dfs = func(node, parent, grandparent *TreeNode) int {
		if node == nil {
			return 0
		}
		add := 0
		if grandparent != nil && grandparent.Val%2 == 0 {
			add = node.Val
		}
		return add + dfs(node.Left, node, parent) + dfs(node.Right, node, parent)
	}
	return dfs(root, nil, nil)
}
