// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	queue := []*TreeNode{root}
	bestSum, bestLevel, level := root.Val, 1, 1
	for len(queue) > 0 {
		sum := 0
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if sum > bestSum {
			bestSum, bestLevel = sum, level
		}
		level++
	}
	return bestLevel
}
