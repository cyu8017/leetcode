// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/


import "sort"

func sumOfPower(nums []int) int {
	const MOD = 1000000007
	sort.Ints(nums)
	ans, s := 0, 0
	for _, x := range nums {
		ans = (ans + x*x%MOD*(s+x)%MOD) % MOD
		s = (2*s + x) % MOD
	}
	return ans
}
