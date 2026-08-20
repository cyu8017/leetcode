// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minimumOperations(root *TreeNode) int {
	if root == nil {
		return 0
	}
	ans := 0
	q := []*TreeNode{root}
	for len(q) > 0 {
		sz := len(q)
		vals := make([]int, sz)
		for i := 0; i < sz; i++ {
			node := q[0]
			q = q[1:]
			vals[i] = node.Val
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		sorted := append([]int{}, vals...)
		sort.Ints(sorted)
		pos := map[int]int{}
		for i, v := range vals {
			pos[v] = i
		}
		for i := 0; i < sz; i++ {
			if vals[i] != sorted[i] {
				j := pos[sorted[i]]
				vals[i], vals[j] = vals[j], vals[i]
				pos[vals[j]] = j
				pos[vals[i]] = i
				ans++
			}
		}
	}
	return ans
}
