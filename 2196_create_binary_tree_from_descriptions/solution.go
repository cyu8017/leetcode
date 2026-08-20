// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	nodes := map[int]*TreeNode{}
	child := map[int]bool{}
	for _, d := range descriptions {
		p, c, isLeft := d[0], d[1], d[2]
		if nodes[p] == nil {
			nodes[p] = &TreeNode{Val: p}
		}
		if nodes[c] == nil {
			nodes[c] = &TreeNode{Val: c}
		}
		if isLeft == 1 {
			nodes[p].Left = nodes[c]
		} else {
			nodes[p].Right = nodes[c]
		}
		child[c] = true
	}
	for v, node := range nodes {
		if !child[v] {
			return node
		}
	}
	return nil
}
