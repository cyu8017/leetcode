// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

import "sort"

func removeCoveredIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	answer, farthest := 0, -1
	for _, iv := range intervals {
		if iv[1] > farthest {
			answer++
			farthest = iv[1]
		}
	}
	return answer
}
