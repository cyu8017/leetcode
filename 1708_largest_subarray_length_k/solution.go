// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

func largestSubarray(nums []int, k int) []int {
	start := 0
	for i := 1; i+k <= len(nums); i++ {
		if nums[i] > nums[start] {
			start = i
		}
	}
	result := make([]int, k)
	copy(result, nums[start:start+k])
	return result
}
