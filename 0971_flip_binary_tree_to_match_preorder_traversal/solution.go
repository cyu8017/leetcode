// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flipMatchVoyage(root *TreeNode, voyage []int) []int {
	i := 0
	ans := []int{}
	var dfs func(*TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		if node.Val != voyage[i] {
			return false
		}
		i++
		if node.Left != nil && i < len(voyage) && node.Left.Val != voyage[i] {
			ans = append(ans, node.Val)
			return dfs(node.Right) && dfs(node.Left)
		}
		return dfs(node.Left) && dfs(node.Right)
	}
	if dfs(root) {
		return ans
	}
	return []int{-1}
}
