// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func nextLargerNodes(head *ListNode) []int {
	vals := []int{}
	for head != nil {
		vals = append(vals, head.Val)
		head = head.Next
	}
	ans := make([]int, len(vals))
	stack := []int{}
	for i, x := range vals {
		for len(stack) > 0 && vals[stack[len(stack)-1]] < x {
			ans[stack[len(stack)-1]] = x
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return ans
}
