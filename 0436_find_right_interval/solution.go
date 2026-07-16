// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

import "sort"

func findRightInterval(intervals [][]int) []int {
	type indexedInterval struct {
		start int
		index int
	}

	indexed := make([]indexedInterval, len(intervals))
	for index, interval := range intervals {
		indexed[index] = indexedInterval{start: interval[0], index: index}
	}
	sort.Slice(indexed, func(i, j int) bool {
		return indexed[i].start < indexed[j].start
	})

	starts := make([]int, len(indexed))
	for index, entry := range indexed {
		starts[index] = entry.start
	}

	result := make([]int, len(intervals))
	for index, interval := range intervals {
		end := interval[1]
		position := sort.SearchInts(starts, end)
		if position == len(starts) {
			result[index] = -1
		} else {
			result[index] = indexed[position].index
		}
	}
	return result
}
