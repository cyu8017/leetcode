// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func balanceBST(root *TreeNode) *TreeNode {
	var nodes []*TreeNode
	var walk func(*TreeNode)
	walk = func(x *TreeNode) {
		if x == nil {
			return
		}
		walk(x.Left)
		nodes = append(nodes, x)
		walk(x.Right)
	}
	walk(root)
	var build func(l, r int) *TreeNode
	build = func(l, r int) *TreeNode {
		if l >= r {
			return nil
		}
		m := (l + r) / 2
		x := nodes[m]
		x.Left = build(l, m)
		x.Right = build(m+1, r)
		return x
	}
	return build(0, len(nodes))
}
