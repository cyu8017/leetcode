// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func printTree(root *TreeNode) [][]string {
	var height func(node *TreeNode) int
	height = func(node *TreeNode) int {
		if node == nil {
			return -1
		}
		lh, rh := height(node.Left), height(node.Right)
		if lh > rh {
			return 1 + lh
		}
		return 1 + rh
	}
	h := height(root)
	rows := h + 1
	cols := (1 << (h + 1)) - 1
	res := make([][]string, rows)
	for i := range res {
		res[i] = make([]string, cols)
	}
	var place func(node *TreeNode, r, c int)
	place = func(node *TreeNode, r, c int) {
		if node == nil {
			return
		}
		res[r][c] = strconv.Itoa(node.Val)
		if r == h {
			return
		}
		offset := 1 << (h - r - 1)
		place(node.Left, r+1, c-offset)
		place(node.Right, r+1, c+offset)
	}
	place(root, 0, (cols-1)/2)
	return res
}
