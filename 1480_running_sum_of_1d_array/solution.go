// LeetCode 1480 - Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/

func runningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	return nums
}
