// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

func maxTotalValue(nums []int, k int) int64 {
	return int64(k * (slices.Max(nums) - slices.Min(nums)))
}
