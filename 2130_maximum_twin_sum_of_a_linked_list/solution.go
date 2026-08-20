// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	var prev *ListNode
	for slow != nil {
		nxt := slow.Next
		slow.Next = prev
		prev = slow
		slow = nxt
	}
	ans := 0
	a, b := head, prev
	for b != nil {
		if a.Val+b.Val > ans {
			ans = a.Val + b.Val
		}
		a = a.Next
		b = b.Next
	}
	return ans
}
