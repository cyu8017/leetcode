// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

func maxAbsoluteSum(nums []int) int {
	prefix := 0
	low := 0
	high := 0
	for _, value := range nums {
		prefix += value
		if prefix < low {
			low = prefix
		}
		if prefix > high {
			high = prefix
		}
	}
	return high - low
}
