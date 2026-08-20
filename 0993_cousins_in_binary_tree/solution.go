// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isCousins(root *TreeNode, x int, y int) bool {
	type info struct {
		depth  int
		parent *TreeNode
	}
	m := map[int]info{}
	var dfs func(*TreeNode, *TreeNode, int)
	dfs = func(node, parent *TreeNode, depth int) {
		if node == nil {
			return
		}
		if node.Val == x || node.Val == y {
			m[node.Val] = info{depth, parent}
		}
		dfs(node.Left, node, depth+1)
		dfs(node.Right, node, depth+1)
	}
	dfs(root, nil, 0)
	return m[x].depth == m[y].depth && m[x].parent != m[y].parent
}
