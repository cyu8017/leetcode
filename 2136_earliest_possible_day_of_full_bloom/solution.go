// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

import "sort"

func earliestFullBloom(plantTime []int, growTime []int) int {
	n := len(plantTime)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return growTime[idx[i]] > growTime[idx[j]] })
	day, ans := 0, 0
	for _, i := range idx {
		day += plantTime[i]
		if day+growTime[i] > ans {
			ans = day + growTime[i]
		}
	}
	return ans
}
