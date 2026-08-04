// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BSTIterator struct {
	values []int
	index  int
}

func Constructor(root *TreeNode) BSTIterator {
	values := []int{}
	stack := []*TreeNode{}
	for len(stack) > 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		values = append(values, root.Val)
		root = root.Right
	}
	return BSTIterator{values: values, index: -1}
}

func (this *BSTIterator) HasNext() bool {
	return this.index+1 < len(this.values)
}

func (this *BSTIterator) Next() int {
	this.index++
	return this.values[this.index]
}

func (this *BSTIterator) HasPrev() bool {
	return this.index > 0
}

func (this *BSTIterator) Prev() int {
	this.index--
	return this.values[this.index]
}
