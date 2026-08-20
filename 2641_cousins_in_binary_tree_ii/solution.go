// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/


type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func replaceValueInTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	root.Val = 0
	q := []*TreeNode{root}
	for len(q) > 0 {
		sz := len(q)
		levelSum := 0
		for i := 0; i < sz; i++ {
			node := q[i]
			if node.Left != nil {
				levelSum += node.Left.Val
			}
			if node.Right != nil {
				levelSum += node.Right.Val
			}
		}
		for i := 0; i < sz; i++ {
			node := q[0]
			q = q[1:]
			cousin := levelSum
			if node.Left != nil {
				cousin -= node.Left.Val
			}
			if node.Right != nil {
				cousin -= node.Right.Val
			}
			if node.Left != nil {
				node.Left.Val = cousin
				q = append(q, node.Left)
			}
			if node.Right != nil {
				node.Right.Val = cousin
				q = append(q, node.Right)
			}
		}
	}
	return root
}
