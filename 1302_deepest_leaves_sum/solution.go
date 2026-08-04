// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deepestLeavesSum(root *TreeNode) int {
	level := []*TreeNode{root}
	answer := 0
	for len(level) > 0 {
		answer = 0
		next := []*TreeNode{}
		for _, node := range level {
			answer += node.Val
			if node.Left != nil {
				next = append(next, node.Left)
			}
			if node.Right != nil {
				next = append(next, node.Right)
			}
		}
		level = next
	}
	return answer
}
