// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

import "sort"

func canAttendMeetings(intervals [][]int) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	for index := 1; index < len(intervals); index++ {
		if intervals[index][0] < intervals[index-1][1] {
			return false
		}
	}
	return true
}
