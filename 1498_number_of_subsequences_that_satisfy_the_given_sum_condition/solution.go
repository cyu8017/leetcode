// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

import "sort"

func numSubseq(nums []int, target int) int {
	sort.Ints(nums)
	const mod = 1000000007
	left, right, ans := 0, len(nums)-1, 0
	powers := make([]int, len(nums)+1)
	powers[0] = 1
	for i := 1; i < len(powers); i++ {
		powers[i] = powers[i-1] * 2 % mod
	}
	for left <= right {
		if nums[left]+nums[right] <= target {
			ans = (ans + powers[right-left]) % mod
			left++
		} else {
			right--
		}
	}
	return ans
}
