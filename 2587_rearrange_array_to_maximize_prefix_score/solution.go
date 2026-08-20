// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/


import "sort"

func maxScore(nums []int) int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	var sum int64
	ans := 0
	for _, x := range nums {
		sum += int64(x)
		if sum > 0 {
			ans++
		} else {
			break
		}
	}
	return ans
}
