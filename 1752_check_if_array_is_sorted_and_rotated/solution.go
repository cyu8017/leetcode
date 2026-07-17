// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

func check(nums []int) bool {
	n := len(nums)
	drops := 0
	for i := 0; i < n; i++ {
		if nums[i] > nums[(i+1)%n] {
			drops++
		}
	}
	return drops <= 1
}
