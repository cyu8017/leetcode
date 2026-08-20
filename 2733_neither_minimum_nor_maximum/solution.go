// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/


func findNonMinOrMax(nums []int) int {
	if len(nums) < 3 {
		return -1
	}
	a, b, c := nums[0], nums[1], nums[2]
	// median of first three
	if (a-b)*(a-c) <= 0 {
		return a
	}
	if (b-a)*(b-c) <= 0 {
		return b
	}
	return c
}
