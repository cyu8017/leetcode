// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

import "sort"

func minimumCost(cost []int) int {
	sort.Slice(cost, func(i, j int) bool { return cost[i] > cost[j] })
	ans := 0
	for i, c := range cost {
		if i%3 != 2 {
			ans += c
		}
	}
	return ans
}
