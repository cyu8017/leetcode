// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	value := 0
	for head != nil {
		value = value*2 + head.Val
		head = head.Next
	}
	return value
}
