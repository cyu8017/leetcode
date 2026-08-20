// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

func finalElement(nums []int) int {
	return max(nums[0], nums[len(nums)-1])
}
