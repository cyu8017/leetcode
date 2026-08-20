// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkEqualTree(root *TreeNode) bool {
	subtreeSums := []int{}
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		total := node.Val + dfs(node.Left) + dfs(node.Right)
		subtreeSums = append(subtreeSums, total)
		return total
	}
	total := dfs(root)
	subtreeSums = subtreeSums[:len(subtreeSums)-1]
	if total%2 != 0 {
		return false
	}
	half := total / 2
	for _, s := range subtreeSums {
		if s == half {
			return true
		}
	}
	return false
}
