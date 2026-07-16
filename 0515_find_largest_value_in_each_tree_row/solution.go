// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	result := make([]int, 0)
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelMax := queue[0].Val
		levelSize := len(queue)
		for index := 0; index < levelSize; index++ {
			node := queue[0]
			queue = queue[1:]
			if node.Val > levelMax {
				levelMax = node.Val
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, levelMax)
	}
	return result
}
