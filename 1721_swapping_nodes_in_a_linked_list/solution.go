// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

type ListNode struct {
    Val  int
    Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {
    first := head
    for i := 0; i < k-1; i++ {
        first = first.Next
    }
    fast := first
    second := head
    for fast.Next != nil {
        fast = fast.Next
        second = second.Next
    }
    first.Val, second.Val = second.Val, first.Val
    return head
}
