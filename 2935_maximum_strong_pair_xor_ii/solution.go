// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

import "sort"

func maximumStrongPairXor(nums []int) int {
	sort.Ints(nums)
	ans := 0
	for i, x := range nums {
		for j := i; j < len(nums) && nums[j] <= 2*x; j++ {
			xorr := x ^ nums[j]
			if xorr > ans {
				ans = xorr
			}
		}
	}
	return ans
}
