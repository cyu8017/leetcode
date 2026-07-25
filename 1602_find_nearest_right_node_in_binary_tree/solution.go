// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findNearestRightNode(root *TreeNode, u *TreeNode) *TreeNode {
	if root == nil || u == nil {
		return nil
	}
	q := []*TreeNode{root}
	for len(q) > 0 {
		nxt := []*TreeNode{}
		for i, node := range q {
			if node == u || node.Val == u.Val {
				if i+1 < len(q) {
					return q[i+1]
				}
				return nil
			}
			if node.Left != nil {
				nxt = append(nxt, node.Left)
			}
			if node.Right != nil {
				nxt = append(nxt, node.Right)
			}
		}
		q = nxt
	}
	return nil
}
