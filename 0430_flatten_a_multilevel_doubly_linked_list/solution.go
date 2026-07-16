// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

type Node struct {
	Val  int
	Prev *Node
	Next *Node
	Child *Node
}

func flatten(head *Node) *Node {
	current := head
	for current != nil {
		if current.Child != nil {
			nextNode := current.Next
			childHead := flatten(current.Child)
			current.Next = childHead
			childHead.Prev = current
			tail := childHead
			for tail.Next != nil {
				tail = tail.Next
			}
			tail.Next = nextNode
			if nextNode != nil {
				nextNode.Prev = tail
			}
			current.Child = nil
		}
		current = current.Next
	}
	return head
}
