// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

type listNode struct {
	val  int
	next *listNode
}

type MyLinkedList struct {
	dummy *listNode
	size  int
}

func Constructor() MyLinkedList {
	return MyLinkedList{dummy: &listNode{}}
}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.size {
		return -1
	}
	node := this.dummy.next
	for i := 0; i < index; i++ {
		node = node.next
	}
	return node.val
}

func (this *MyLinkedList) AddAtHead(val int) {
	this.AddAtIndex(0, val)
}

func (this *MyLinkedList) AddAtTail(val int) {
	this.AddAtIndex(this.size, val)
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.size {
		return
	}
	prev := this.dummy
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	node := &listNode{val: val, next: prev.next}
	prev.next = node
	this.size++
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.size {
		return
	}
	prev := this.dummy
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	prev.next = prev.next.next
	this.size--
}
