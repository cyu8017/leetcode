// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

import (
	"sort"
	"strconv"
	"strings"
)

func findMinDifference(timePoints []string) int {
	minutes := make([]int, len(timePoints))
	for index, time := range timePoints {
		parts := strings.Split(time, ":")
		hour, _ := strconv.Atoi(parts[0])
		minute, _ := strconv.Atoi(parts[1])
		minutes[index] = hour*60 + minute
	}

	sort.Ints(minutes)
	best := minutes[len(minutes)-1] - minutes[0]
	for index := 1; index < len(minutes); index++ {
		if diff := minutes[index] - minutes[index-1]; diff < best {
			best = diff
		}
	}
	if wrap := 24*60 - minutes[len(minutes)-1] + minutes[0]; wrap < best {
		best = wrap
	}
	return best
}
