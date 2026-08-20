// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfSubtree(root *TreeNode) int {
	ans := 0
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}
		ls, lc := dfs(node.Left)
		rs, rc := dfs(node.Right)
		sum := ls + rs + node.Val
		cnt := lc + rc + 1
		if sum/cnt == node.Val {
			ans++
		}
		return sum, cnt
	}
	dfs(root)
	return ans
}
