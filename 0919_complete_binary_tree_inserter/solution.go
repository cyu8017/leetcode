// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type CBTInserter struct {
	root  *TreeNode
	queue []*TreeNode
}

func Constructor(root *TreeNode) CBTInserter {
	ci := CBTInserter{root: root}
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node.Left != nil {
			q = append(q, node.Left)
		} else {
			ci.queue = append(ci.queue, node)
			break
		}
		if node.Right != nil {
			q = append(q, node.Right)
		} else {
			ci.queue = append(ci.queue, node)
			break
		}
	}
	ci.queue = append(ci.queue, q...)
	return ci
}

func (this *CBTInserter) Insert(val int) int {
	parent := this.queue[0]
	child := &TreeNode{Val: val}
	if parent.Left == nil {
		parent.Left = child
	} else {
		parent.Right = child
		this.queue = this.queue[1:]
	}
	this.queue = append(this.queue, child)
	return parent.Val
}

func (this *CBTInserter) GetRoot() *TreeNode {
	return this.root
}
