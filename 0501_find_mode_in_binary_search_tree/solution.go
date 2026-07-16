// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findMode(root *TreeNode) []int {
	counts := map[int]int{}
	best := 0

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		counts[node.Val]++
		if counts[node.Val] > best {
			best = counts[node.Val]
		}
		inorder(node.Right)
	}
	inorder(root)

	result := make([]int, 0)
	for value, count := range counts {
		if count == best {
			result = append(result, value)
		}
	}
	return result
}
