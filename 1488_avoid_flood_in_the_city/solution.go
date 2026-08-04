// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

import "sort"

func avoidFlood(rains []int) []int {
	ans := make([]int, len(rains))
	for i := range ans {
		ans[i] = -1
	}
	full := map[int]int{}
	dry := []int{}
	for i, lake := range rains {
		if lake == 0 {
			dry = append(dry, i)
			ans[i] = 1
		} else {
			if prev, ok := full[lake]; ok {
				j := sort.SearchInts(dry, prev+1)
				if j == len(dry) {
					return []int{}
				}
				ans[dry[j]] = lake
				dry = append(dry[:j], dry[j+1:]...)
			}
			full[lake] = i
		}
	}
	return ans
}
