// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

type ImmutableListNode interface {
	GetNext() ImmutableListNode
	PrintValue()
}

func printLinkedListInReverse(head ImmutableListNode) {
	if head == nil {
		return
	}
	printLinkedListInReverse(head.GetNext())
	head.PrintValue()
}
