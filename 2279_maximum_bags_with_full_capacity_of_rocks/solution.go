// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

import "sort"

func maximumBags(capacity []int, rocks []int, additionalRocks int) int {
	need := make([]int, len(capacity))
	for i := range capacity {
		need[i] = capacity[i] - rocks[i]
	}
	sort.Ints(need)
	ans := 0
	for _, n := range need {
		if additionalRocks < n {
			break
		}
		additionalRocks -= n
		ans++
	}
	return ans
}
