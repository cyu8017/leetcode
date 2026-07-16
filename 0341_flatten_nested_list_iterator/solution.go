// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

type NestedInteger struct {
	integer *int
	list    []*NestedInteger
}

func (n NestedInteger) IsInteger() bool {
	return n.integer != nil
}

func (n NestedInteger) GetInteger() int {
	if n.integer == nil {
		return 0
	}
	return *n.integer
}

func (n NestedInteger) GetList() []*NestedInteger {
	return n.list
}

type frame struct {
	node  *NestedInteger
	index int
}

type NestedIterator struct {
	stack []frame
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	iter := &NestedIterator{}
	for index := len(nestedList) - 1; index >= 0; index-- {
		iter.stack = append(iter.stack, frame{node: nestedList[index], index: 0})
	}
	return iter
}

func (this *NestedIterator) prepareNext() {
	for len(this.stack) > 0 {
		current := this.stack[len(this.stack)-1]
		if current.node.IsInteger() {
			return
		}
		nested := current.node.GetList()
		if current.index >= len(nested) {
			this.stack = this.stack[:len(this.stack)-1]
			continue
		}
		this.stack[len(this.stack)-1].index = current.index + 1
		this.stack = append(this.stack, frame{node: nested[current.index], index: 0})
	}
}

func (this *NestedIterator) advance(nested []*NestedInteger) int {
	for index := len(nested) - 1; index >= 0; index-- {
		this.stack = append(this.stack, frame{node: nested[index], index: 0})
	}
	this.prepareNext()
	current := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	if current.node.IsInteger() {
		return current.node.GetInteger()
	}
	return this.advance(current.node.GetList())
}

func (this *NestedIterator) Next() int {
	current := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	if current.node.IsInteger() {
		return current.node.GetInteger()
	}
	return this.advance(current.node.GetList())
}

func (this *NestedIterator) HasNext() bool {
	this.prepareNext()
	return len(this.stack) > 0
}
