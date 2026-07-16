// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findFrequentTreeSum(root *TreeNode) []int {
	counts := map[int]int{}

	var subtreeSum func(node *TreeNode) int
	subtreeSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		total := node.Val + subtreeSum(node.Left) + subtreeSum(node.Right)
		counts[total]++
		return total
	}
	subtreeSum(root)

	if len(counts) == 0 {
		return []int{}
	}
	best := 0
	for _, count := range counts {
		if count > best {
			best = count
		}
	}
	result := make([]int, 0)
	for value, count := range counts {
		if count == best {
			result = append(result, value)
		}
	}
	sort.Ints(result)
	return result
}
