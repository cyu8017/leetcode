// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

func wiggleMaxLength(nums []int) int {
	if len(nums) < 2 {
		return len(nums)
	}

	up := 1
	down := 1
	for index := 1; index < len(nums); index++ {
		if nums[index] > nums[index-1] {
			up = down + 1
		} else if nums[index] < nums[index-1] {
			down = up + 1
		}
	}

	if up > down {
		return up
	}
	return down
}
