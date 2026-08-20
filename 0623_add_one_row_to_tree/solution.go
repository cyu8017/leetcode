// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		return &TreeNode{Val: val, Left: root}
	}
	var dfs func(node *TreeNode, current int)
	dfs = func(node *TreeNode, current int) {
		if node == nil {
			return
		}
		if current == depth-1 {
			node.Left = &TreeNode{Val: val, Left: node.Left}
			node.Right = &TreeNode{Val: val, Right: node.Right}
			return
		}
		dfs(node.Left, current+1)
		dfs(node.Right, current+1)
	}
	dfs(root, 1)
	return root
}
