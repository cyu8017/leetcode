// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

import "sort"

func intersectionSizeTwo(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] < intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})
	size := 0
	first, second := -1, -1
	for _, iv := range intervals {
		left, right := iv[0], iv[1]
		if left <= first {
			continue
		}
		if left <= second {
			size++
			first, second = second, right
		} else {
			size += 2
			first, second = right-1, right
		}
	}
	return size
}
