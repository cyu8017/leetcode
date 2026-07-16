// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedListToBST(head *ListNode) *TreeNode {
	values := []int{}
	for head != nil {
		values = append(values, head.Val)
		head = head.Next
	}

	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		mid := (left + right + 1) / 2
		root := &TreeNode{Val: values[mid]}
		root.Left = build(left, mid-1)
		root.Right = build(mid+1, right)
		return root
	}

	return build(0, len(values)-1)
}
