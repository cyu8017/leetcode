// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

import "sort"

func findMinArrowShots(points [][]int) int {
	if len(points) == 0 {
		return 0
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})

	arrows := 1
	end := points[0][1]
	for index := 1; index < len(points); index++ {
		if points[index][0] > end {
			arrows++
			end = points[index][1]
		}
	}
	return arrows
}
