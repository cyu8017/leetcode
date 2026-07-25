// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeInBetween(list1 *ListNode, a, b int, list2 *ListNode) *ListNode {
	pre := list1
	for i := 0; i < a-1; i++ {
		pre = pre.Next
	}
	post := pre
	for i := 0; i < b-a+2; i++ {
		post = post.Next
	}
	pre.Next = list2
	for pre.Next != nil {
		pre = pre.Next
	}
	pre.Next = post
	return list1
}
