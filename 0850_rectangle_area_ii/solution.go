// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

import "sort"

func rectangleArea(rectangles [][]int) int {
	const MOD = 1_000_000_007
	type event struct{ x, typ, y1, y2 int }
	events := make([]event, 0, len(rectangles)*2)
	for _, r := range rectangles {
		x1, y1, x2, y2 := r[0], r[1], r[2], r[3]
		events = append(events, event{x1, 1, y1, y2}, event{x2, -1, y1, y2})
	}
	sort.Slice(events, func(i, j int) bool { return events[i].x < events[j].x })

	coveredLength := func(active [][2]int) int {
		if len(active) == 0 {
			return 0
		}
		sort.Slice(active, func(i, j int) bool {
			if active[i][0] != active[j][0] {
				return active[i][0] < active[j][0]
			}
			return active[i][1] < active[j][1]
		})
		total := 0
		curStart, curEnd := active[0][0], active[0][1]
		for _, seg := range active[1:] {
			start, end := seg[0], seg[1]
			if start > curEnd {
				total += curEnd - curStart
				curStart, curEnd = start, end
			} else if end > curEnd {
				curEnd = end
			}
		}
		total += curEnd - curStart
		return total
	}

	active := [][2]int{}
	area := 0
	prevX := events[0].x
	for _, e := range events {
		area += coveredLength(active) * (e.x - prevX)
		if e.typ == 1 {
			active = append(active, [2]int{e.y1, e.y2})
		} else {
			for i, seg := range active {
				if seg[0] == e.y1 && seg[1] == e.y2 {
					active = append(active[:i], active[i+1:]...)
					break
				}
			}
		}
		prevX = e.x
	}
	return area % MOD
}
