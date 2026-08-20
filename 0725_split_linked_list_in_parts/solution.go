// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

type ListNode struct {
	Val  int
	Next *ListNode
}

func splitListToParts(head *ListNode, k int) []*ListNode {
	length := 0
	for node := head; node != nil; node = node.Next {
		length++
	}
	partSize, extra := length/k, length%k
	result := make([]*ListNode, k)
	current := head
	for i := 0; i < k; i++ {
		result[i] = current
		size := partSize
		if i < extra {
			size++
		}
		for j := 0; j < size-1; j++ {
			if current != nil {
				current = current.Next
			}
		}
		if current != nil {
			nxt := current.Next
			current.Next = nil
			current = nxt
		}
	}
	return result
}
