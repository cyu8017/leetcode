// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

import "sort"

func averageHeightOfBuildings(buildings [][]int) [][]int {
	type event struct{ x, d, h int }
	events := make([]event, 0, len(buildings)*2)
	for _, b := range buildings {
		events = append(events, event{b[0], 1, b[2]}, event{b[1], -1, b[2]})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].x != events[j].x {
			return events[i].x < events[j].x
		}
		return events[i].d < events[j].d
	})
	ans := [][]int{}
	count, sum, prev := 0, 0, events[0].x
	for _, e := range events {
		if e.x != prev && count > 0 {
			avg := sum / count
			if len(ans) > 0 && ans[len(ans)-1][1] == prev && ans[len(ans)-1][2] == avg {
				ans[len(ans)-1][1] = e.x
			} else {
				ans = append(ans, []int{prev, e.x, avg})
			}
		}
		count += e.d
		sum += e.d * e.h
		prev = e.x
	}
	return ans
}
