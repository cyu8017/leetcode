// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/


import "sort"

func countWays(ranges [][]int) int {
	const MOD = 1000000007
	sort.Slice(ranges, func(i, j int) bool { return ranges[i][0] < ranges[j][0] })
	groups := 0
	end := -1
	for _, r := range ranges {
		if r[0] > end {
			groups++
			end = r[1]
		} else if r[1] > end {
			end = r[1]
		}
	}
	ans := 1
	for i := 0; i < groups; i++ {
		ans = ans * 2 % MOD
	}
	return ans
}
