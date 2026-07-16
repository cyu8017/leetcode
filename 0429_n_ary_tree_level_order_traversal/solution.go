// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) [][]int {
	if root == nil {
		return [][]int{}
	}

	result := make([][]int, 0)
	queue := []*Node{root}

	for len(queue) > 0 {
		size := len(queue)
		level := make([]int, 0, size)
		for index := 0; index < size; index++ {
			node := queue[0]
			queue = queue[1:]
			level = append(level, node.Val)
			queue = append(queue, node.Children...)
		}
		result = append(result, level)
	}

	return result
}
