// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/


import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthLargestLevelSum(root *TreeNode, k int) int64 {
	if root == nil {
		return -1
	}
	sums := []int64{}
	q := []*TreeNode{root}
	for len(q) > 0 {
		sz := len(q)
		var s int64
		for i := 0; i < sz; i++ {
			node := q[0]
			q = q[1:]
			s += int64(node.Val)
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		sums = append(sums, s)
	}
	sort.Slice(sums, func(i, j int) bool { return sums[i] > sums[j] })
	if k > len(sums) {
		return -1
	}
	return sums[k-1]
}
