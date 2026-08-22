// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

func maximizeScore(nums []int) int {
	// score is sum of deleted pair adjacent; maximize by leaving minimum possible
	n := len(nums)
	total := 0
	for _, x := range nums {
		total += x
	}
	if n%2 == 1 {
		mn := nums[0]
		for _, x := range nums {
			if x < mn {
				mn = x
			}
		}
		return total - mn
	}
	mn := nums[0] + nums[1]
	for i := 0; i+1 < n; i++ {
		if nums[i]+nums[i+1] < mn {
			mn = nums[i] + nums[i+1]
		}
	}
	return total - mn
}
