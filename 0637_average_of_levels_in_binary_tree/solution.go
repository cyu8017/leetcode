// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return nil
	}
	result := []float64{}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		count := len(queue)
		total := 0
		for i := 0; i < count; i++ {
			node := queue[0]
			queue = queue[1:]
			total += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, float64(total)/float64(count))
	}
	return result
}
