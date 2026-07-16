// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

import "sort"

func eraseOverlapIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	removed := 0
	end := -1 << 30
	for _, interval := range intervals {
		if interval[0] < end {
			removed++
		} else {
			end = interval[1]
		}
	}
	return removed
}
