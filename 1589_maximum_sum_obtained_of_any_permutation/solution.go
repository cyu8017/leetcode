// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

import "sort"

func maxSumRangeQuery(nums []int, requests [][]int) int {
	const MOD = 1_000_000_007
	diff := make([]int, len(nums)+1)
	for _, r := range requests {
		diff[r[0]]++
		diff[r[1]+1]--
	}
	for i := 1; i < len(nums); i++ {
		diff[i] += diff[i-1]
	}
	freq := diff[:len(nums)]
	sort.Ints(nums)
	sort.Ints(freq)
	ans := 0
	for i := 0; i < len(nums); i++ {
		ans = (ans + nums[i]*freq[i]) % MOD
	}
	return ans
}
