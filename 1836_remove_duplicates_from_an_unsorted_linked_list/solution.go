// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicatesUnsorted(head *ListNode) *ListNode {
	counts := map[int]int{}
	node := head
	for node != nil {
		counts[node.Val]++
		node = node.Next
	}

	dummy := &ListNode{Next: head}
	prev := dummy
	node = head
	for node != nil {
		if counts[node.Val] > 1 {
			prev.Next = node.Next
			node = node.Next
		} else {
			prev = node
			node = node.Next
		}
	}
	return dummy.Next
}
