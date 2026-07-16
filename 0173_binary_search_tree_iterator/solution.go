// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

type BSTIterator struct {
	stack []*TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
	iterator := BSTIterator{}
	iterator.pushLeft(root)
	return iterator
}

func (this *BSTIterator) pushLeft(node *TreeNode) {
	for node != nil {
		this.stack = append(this.stack, node)
		node = node.Left
	}
}

func (this *BSTIterator) Next() int {
	last := len(this.stack) - 1
	node := this.stack[last]
	this.stack = this.stack[:last]
	this.pushLeft(node.Right)
	return node.Val
}

func (this *BSTIterator) HasNext() bool {
	return len(this.stack) > 0
}