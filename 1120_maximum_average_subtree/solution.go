// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maximumAverageSubtree(root *TreeNode) float64 {
	best := 0.0
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}
		ls, lc := dfs(node.Left)
		rs, rc := dfs(node.Right)
		totalSum := ls + rs + node.Val
		totalCount := lc + rc + 1
		avg := float64(totalSum) / float64(totalCount)
		if avg > best {
			best = avg
		}
		return totalSum, totalCount
	}
	dfs(root)
	return best
}
