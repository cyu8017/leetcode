// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

import "sort"

func minMeetingRooms(intervals [][]int) int {
	starts := make([]int, len(intervals))
	ends := make([]int, len(intervals))
	for index, interval := range intervals {
		starts[index] = interval[0]
		ends[index] = interval[1]
	}
	sort.Ints(starts)
	sort.Ints(ends)

	rooms := 0
	maxRooms := 0
	startIndex := 0
	endIndex := 0
	for startIndex < len(starts) {
		if starts[startIndex] < ends[endIndex] {
			rooms++
			if rooms > maxRooms {
				maxRooms = rooms
			}
			startIndex++
		} else {
			rooms--
			endIndex++
		}
	}
	return maxRooms
}
