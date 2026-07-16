// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

func maxSubArray(nums []int) int {
	best := nums[0]
	current := nums[0]

	for i := 1; i < len(nums); i++ {
		if current+nums[i] > nums[i] {
			current += nums[i]
		} else {
			current = nums[i]
		}
		if current > best {
			best = current
		}
	}

	return best
}
