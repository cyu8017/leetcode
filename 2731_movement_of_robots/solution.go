// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/


import "sort"

func sumDistance(nums []int, s string, d int) int {
	const MOD = 1000000007
	n := len(nums)
	pos := make([]int, n)
	for i := 0; i < n; i++ {
		if s[i] == 'R' {
			pos[i] = nums[i] + d
		} else {
			pos[i] = nums[i] - d
		}
	}
	sort.Ints(pos)
	ans, pref := 0, 0
	for i, p := range pos {
		ans = (ans + i*p%MOD - pref + MOD) % MOD
		pref = (pref + p) % MOD
	}
	return ans
}
