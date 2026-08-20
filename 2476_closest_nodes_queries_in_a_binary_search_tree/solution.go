// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func closestNodes(root *TreeNode, queries []int) [][]int {
	vals := []int{}
	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		vals = append(vals, node.Val)
		inorder(node.Right)
	}
	inorder(root)
	ans := make([][]int, len(queries))
	for i, q := range queries {
		j := sort.SearchInts(vals, q)
		mx := -1
		if j < len(vals) {
			mx = vals[j]
		}
		mn := -1
		if j < len(vals) && vals[j] == q {
			mn = q
		} else if j > 0 {
			mn = vals[j-1]
		}
		ans[i] = []int{mn, mx}
	}
	return ans
}
