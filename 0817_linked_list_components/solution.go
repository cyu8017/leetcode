// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

type ListNode struct {
	Val  int
	Next *ListNode
}

func numComponents(head *ListNode, nums []int) int {
	present := map[int]bool{}
	for _, v := range nums {
		present[v] = true
	}
	count := 0
	connected := false
	for head != nil {
		if present[head.Val] {
			if !connected {
				count++
				connected = true
			}
		} else {
			connected = false
		}
		head = head.Next
	}
	return count
}
