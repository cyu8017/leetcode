// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findBottomLeftValue(root *TreeNode) int {
	queue := []*TreeNode{root}
	leftmost := root.Val
	for len(queue) > 0 {
		levelSize := len(queue)
		for index := 0; index < levelSize; index++ {
			node := queue[0]
			queue = queue[1:]
			if index == 0 {
				leftmost = node.Val
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return leftmost
}
