// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getLonelyNodes(root *TreeNode) []int {
	var ans []int
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		if (node.Left == nil) != (node.Right == nil) {
			if node.Left != nil {
				ans = append(ans, node.Left.Val)
			} else {
				ans = append(ans, node.Right.Val)
			}
		}
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return ans
}
