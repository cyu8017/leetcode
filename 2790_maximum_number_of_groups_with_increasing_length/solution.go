// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

import "sort"

func maxIncreasingGroups(usageLimits []int) int {
	sort.Ints(usageLimits)
	ans := 0
	sum := int64(0)
	for _, v := range usageLimits {
		sum += int64(v)
		need := int64(ans+1) * int64(ans+2) / 2
		if sum >= need {
			ans++
		}
	}
	return ans
}
