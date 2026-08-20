// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

type ListNode struct {
	Val  int
	Next *ListNode
}

func nodesBetweenCriticalPoints(head *ListNode) []int {
	crit := []int{}
	prev := head
	cur := head.Next
	idx := 1
	for cur != nil && cur.Next != nil {
		if (cur.Val > prev.Val && cur.Val > cur.Next.Val) || (cur.Val < prev.Val && cur.Val < cur.Next.Val) {
			crit = append(crit, idx)
		}
		prev = cur
		cur = cur.Next
		idx++
	}
	if len(crit) < 2 {
		return []int{-1, -1}
	}
	mn := crit[1] - crit[0]
	for i := 2; i < len(crit); i++ {
		if crit[i]-crit[i-1] < mn {
			mn = crit[i] - crit[i-1]
		}
	}
	return []int{mn, crit[len(crit)-1] - crit[0]}
}
