// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

import "sort"

func brightestPosition(lights [][]int) int {
	type event struct{ x, d int }
	events := make([]event, 0, len(lights)*2)
	for _, light := range lights {
		pos, r := light[0], light[1]
		events = append(events, event{pos - r, 1}, event{pos + r + 1, -1})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].x != events[j].x {
			return events[i].x < events[j].x
		}
		return events[i].d > events[j].d
	})
	best, cur, ans := 0, 0, 0
	for _, e := range events {
		cur += e.d
		if cur > best {
			best = cur
			ans = e.x
		}
	}
	return ans
}
