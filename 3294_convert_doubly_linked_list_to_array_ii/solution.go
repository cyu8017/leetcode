// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

type Node struct {
	Val        int
	Prev, Next *Node
}

func toArray(node *Node) []int {
	for node != nil && node.Prev != nil {
		node = node.Prev
	}
	ans := []int{}
	for node != nil {
		ans = append(ans, node.Val)
		node = node.Next
	}
	return ans
}
