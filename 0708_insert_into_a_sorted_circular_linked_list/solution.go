// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

type Node struct {
	Val  int
	Next *Node
}

func insert(head *Node, insertVal int) *Node {
	node := &Node{Val: insertVal}
	if head == nil {
		node.Next = node
		return node
	}
	cur := head
	for cur.Next != nil && cur.Next != head {
		cur = cur.Next
	}
	cur.Next = head
	prev, curr := head, head.Next
	for {
		if prev.Val <= insertVal && insertVal <= curr.Val {
			break
		}
		if prev.Val > curr.Val && (insertVal >= prev.Val || insertVal <= curr.Val) {
			break
		}
		prev, curr = curr, curr.Next
		if prev == head {
			break
		}
	}
	prev.Next = node
	node.Next = curr
	return head
}
