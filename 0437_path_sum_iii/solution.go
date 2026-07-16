// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	prefixCounts := map[int64]int{0: 1}

	var dfs func(node *TreeNode, current int64) int
	dfs = func(node *TreeNode, current int64) int {
		if node == nil {
			return 0
		}

		current += int64(node.Val)
		total := prefixCounts[current-int64(targetSum)]
		prefixCounts[current]++

		total += dfs(node.Left, current)
		total += dfs(node.Right, current)

		prefixCounts[current]--
		return total
	}

	return dfs(root, 0)
}
