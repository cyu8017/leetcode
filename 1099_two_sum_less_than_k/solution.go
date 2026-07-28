// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

import "sort"

func twoSumLessThanK(nums []int, k int) int {
	sort.Ints(nums)
	lo, hi := 0, len(nums)-1
	ans := -1
	for lo < hi {
		total := nums[lo] + nums[hi]
		if total < k {
			if total > ans {
				ans = total
			}
			lo++
		} else {
			hi--
		}
	}
	return ans
}
