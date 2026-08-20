// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

func findLengthOfLCIS(nums []int) int {
	best, cur := 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			cur++
			if cur > best {
				best = cur
			}
		} else {
			cur = 1
		}
	}
	return best
}
