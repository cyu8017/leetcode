// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	cur := head
	for cur != nil && cur.Next != nil {
		g := gcd(cur.Val, cur.Next.Val)
		node := &ListNode{Val: g, Next: cur.Next}
		cur.Next = node
		cur = node.Next
	}
	return head
}
