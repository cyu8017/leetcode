// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func verticalTraversal(root *TreeNode) [][]int {
	type item struct{ col, row, val int }
	nodes := []item{}
	var dfs func(*TreeNode, int, int)
	dfs = func(node *TreeNode, row, col int) {
		if node == nil {
			return
		}
		nodes = append(nodes, item{col, row, node.Val})
		dfs(node.Left, row+1, col-1)
		dfs(node.Right, row+1, col+1)
	}
	dfs(root, 0, 0)
	sort.Slice(nodes, func(i, j int) bool {
		if nodes[i].col != nodes[j].col {
			return nodes[i].col < nodes[j].col
		}
		if nodes[i].row != nodes[j].row {
			return nodes[i].row < nodes[j].row
		}
		return nodes[i].val < nodes[j].val
	})
	ansMap := map[int][]int{}
	cols := []int{}
	seen := map[int]bool{}
	for _, it := range nodes {
		ansMap[it.col] = append(ansMap[it.col], it.val)
		if !seen[it.col] {
			seen[it.col] = true
			cols = append(cols, it.col)
		}
	}
	sort.Ints(cols)
	ans := make([][]int, len(cols))
	for i, c := range cols {
		ans[i] = ansMap[c]
	}
	return ans
}
