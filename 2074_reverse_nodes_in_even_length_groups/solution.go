// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseEvenLengthGroups(head *ListNode) *ListNode {
	dummy := &ListNode{Next: head}
	prev := dummy
	group := 1
	for prev.Next != nil {
		cur := prev.Next
		cnt := 0
		node := cur
		for node != nil && cnt < group {
			node = node.Next
			cnt++
		}
		if cnt%2 == 0 {
			// reverse cnt nodes
			revPrev := node
			p := cur
			for i := 0; i < cnt; i++ {
				nxt := p.Next
				p.Next = revPrev
				revPrev = p
				p = nxt
			}
			prev.Next = revPrev
			prev = cur
		} else {
			for i := 0; i < cnt; i++ {
				prev = prev.Next
			}
		}
		group++
	}
	return dummy.Next
}
