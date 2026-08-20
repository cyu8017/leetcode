// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

import "sort"

func minCost(nums []int, cost []int) int64 {
	n := len(nums)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return nums[idx[i]] < nums[idx[j]] })
	var totalCost int64
	for _, c := range cost {
		totalCost += int64(c)
	}
	var pref int64
	median := 0
	for _, i := range idx {
		pref += int64(cost[i])
		if pref*2 >= totalCost {
			median = nums[i]
			break
		}
	}
	var ans int64
	for i := 0; i < n; i++ {
		diff := nums[i] - median
		if diff < 0 {
			diff = -diff
		}
		ans += int64(diff) * int64(cost[i])
	}
	return ans
}
