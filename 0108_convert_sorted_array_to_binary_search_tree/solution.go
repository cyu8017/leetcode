// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		mid := (left + right + 1) / 2
		root := &TreeNode{Val: nums[mid]}
		root.Left = build(left, mid-1)
		root.Right = build(mid+1, right)
		return root
	}
	return build(0, len(nums)-1)
}
