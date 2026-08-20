// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

import "sort"

func minConnectedGroups(intervals [][]int, k int) int {
	sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })
	merged := [][]int{}
	for _, it := range intervals {
		if len(merged) == 0 || it[0] > merged[len(merged)-1][1] {
			merged = append(merged, []int{it[0], it[1]})
		} else if it[1] > merged[len(merged)-1][1] {
			merged[len(merged)-1][1] = it[1]
		}
	}
	m := len(merged)
	ans := m
	for i := 0; i < m; i++ {
		// insert interval covering from merged[i] with length involving k
		end := merged[i][1] + k
		j := i
		for j < m && merged[j][0] <= end {
			j++
		}
		// groups: before i, 1 merged group, after j-1
		groups := i + 1 + (m - j)
		if groups < ans {
			ans = groups
		}
	}
	return ans
}
