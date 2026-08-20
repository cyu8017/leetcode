// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

import "sort"

func minGroups(intervals [][]int) int {
	events := make([][2]int, 0, len(intervals)*2)
	for _, it := range intervals {
		events = append(events, [2]int{it[0], 1})
		events = append(events, [2]int{it[1] + 1, -1})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i][0] == events[j][0] {
			return events[i][1] < events[j][1]
		}
		return events[i][0] < events[j][0]
	})
	cur, ans := 0, 0
	for _, e := range events {
		cur += e[1]
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
