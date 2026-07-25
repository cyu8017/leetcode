// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isEvenOddTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	q := []*TreeNode{root}
	level := 0
	for len(q) > 0 {
		prev := 0
		if level%2 == 0 {
			prev = -1 << 30
		} else {
			prev = 1 << 30
		}
		nxt := []*TreeNode{}
		for _, node := range q {
			if node.Val%2 == level%2 {
				return false
			}
			if level%2 == 0 && node.Val <= prev {
				return false
			}
			if level%2 == 1 && node.Val >= prev {
				return false
			}
			prev = node.Val
			if node.Left != nil {
				nxt = append(nxt, node.Left)
			}
			if node.Right != nil {
				nxt = append(nxt, node.Right)
			}
		}
		q = nxt
		level++
	}
	return true
}
