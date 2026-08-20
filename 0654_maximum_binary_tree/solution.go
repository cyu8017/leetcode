// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	var build func(left, right int) *TreeNode
	build = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}
		mid := left
		for i := left; i <= right; i++ {
			if nums[i] > nums[mid] {
				mid = i
			}
		}
		return &TreeNode{Val: nums[mid], Left: build(left, mid-1), Right: build(mid+1, right)}
	}
	return build(0, len(nums)-1)
}
