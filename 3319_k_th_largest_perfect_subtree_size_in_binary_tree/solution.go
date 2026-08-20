// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

import "sort"

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

func kthLargestPerfectSubtree(root *TreeNode, k int) int {
	sizes := []int{}
	var dfs func(*TreeNode) (int, int, bool) // height, size, perfect
	dfs = func(node *TreeNode) (int, int, bool) {
		if node == nil {
			return 0, 0, true
		}
		lh, ls, lp := dfs(node.Left)
		rh, rs, rp := dfs(node.Right)
		sz := ls + rs + 1
		perf := lp && rp && lh == rh
		if perf {
			sizes = append(sizes, sz)
		}
		h := lh
		if rh > h {
			h = rh
		}
		return h + 1, sz, perf
	}
	dfs(root)
	sort.Sort(sort.Reverse(sort.IntSlice(sizes)))
	if k > len(sizes) {
		return -1
	}
	return sizes[k-1]
}
