// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

func maxAscendingSum(nums []int) int {
	best := nums[0]
	cur := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			cur += nums[i]
		} else {
			cur = nums[i]
		}
		if cur > best {
			best = cur
		}
	}
	return best
}
