// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func verticalOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	type queueEntry struct {
		node   *TreeNode
		column int
	}

	columns := make(map[int][]int)
	queue := []queueEntry{{root, 0}}
	minCol := 0
	maxCol := 0

	for len(queue) > 0 {
		entry := queue[0]
		queue = queue[1:]
		node := entry.node
		column := entry.column
		if column < minCol {
			minCol = column
		}
		if column > maxCol {
			maxCol = column
		}
		columns[column] = append(columns[column], node.Val)
		if node.Left != nil {
			queue = append(queue, queueEntry{node.Left, column - 1})
		}
		if node.Right != nil {
			queue = append(queue, queueEntry{node.Right, column + 1})
		}
	}

	result := make([][]int, 0, maxCol-minCol+1)
	for column := minCol; column <= maxCol; column++ {
		result = append(result, columns[column])
	}
	return result
}
