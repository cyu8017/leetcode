// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

func numberOfGoodSubarraySplits(nums []int) int {
	const mod = 1_000_000_007
	ones := make([]int, 0)
	for i, v := range nums {
		if v == 1 {
			ones = append(ones, i)
		}
	}
	if len(ones) == 0 {
		return 0
	}
	ans := 1
	for i := 1; i < len(ones); i++ {
		ans = ans * (ones[i] - ones[i-1]) % mod
	}
	return ans
}
