// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return nil
	}
	return build(1, n)
}

func build(start, end int) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}
	trees := []*TreeNode{}
	for rootVal := start; rootVal <= end; rootVal++ {
		leftTrees := build(start, rootVal-1)
		rightTrees := build(rootVal+1, end)
		for _, left := range leftTrees {
			for _, right := range rightTrees {
				trees = append(trees, &TreeNode{Val: rootVal, Left: left, Right: right})
			}
		}
	}
	return trees
}
