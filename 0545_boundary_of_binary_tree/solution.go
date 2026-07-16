// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func boundaryOfBinaryTree(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	isLeaf := func(node *TreeNode) bool {
		return node != nil && node.Left == nil && node.Right == nil
	}

	var leftBoundary func(node *TreeNode) []int
	leftBoundary = func(node *TreeNode) []int {
		if node == nil || isLeaf(node) {
			return []int{}
		}
		if node.Left != nil {
			return append([]int{node.Val}, leftBoundary(node.Left)...)
		}
		return append([]int{node.Val}, leftBoundary(node.Right)...)
	}

	var rightBoundary func(node *TreeNode) []int
	rightBoundary = func(node *TreeNode) []int {
		if node == nil || isLeaf(node) {
			return []int{}
		}
		if node.Right != nil {
			return append(rightBoundary(node.Right), node.Val)
		}
		return append(rightBoundary(node.Left), node.Val)
	}

	var leaves func(node *TreeNode) []int
	leaves = func(node *TreeNode) []int {
		if node == nil {
			return []int{}
		}
		if isLeaf(node) {
			return []int{node.Val}
		}
		return append(leaves(node.Left), leaves(node.Right)...)
	}

	if isLeaf(root) {
		return []int{root.Val}
	}

	result := []int{root.Val}
	result = append(result, leftBoundary(root.Left)...)
	result = append(result, leaves(root)...)
	result = append(result, rightBoundary(root.Right)...)
	return result
}
