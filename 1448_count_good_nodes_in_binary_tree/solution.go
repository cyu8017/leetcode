// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	var visit func(*TreeNode, int) int
	visit = func(node *TreeNode, maximum int) int {
		if node == nil {
			return 0
		}
		good := 0
		if node.Val >= maximum {
			good = 1
			maximum = node.Val
		}
		return good + visit(node.Left, maximum) + visit(node.Right, maximum)
	}
	return visit(root, int(-1e9))
}
