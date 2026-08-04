// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

import "sort"

func minAvailableDuration(slots1 [][]int, slots2 [][]int, duration int) []int {
	sort.Slice(slots1, func(i, j int) bool { return slots1[i][0] < slots1[j][0] })
	sort.Slice(slots2, func(i, j int) bool { return slots2[i][0] < slots2[j][0] })
	i, j := 0, 0
	for i < len(slots1) && j < len(slots2) {
		start := slots1[i][0]
		if slots2[j][0] > start {
			start = slots2[j][0]
		}
		end := slots1[i][1]
		if slots2[j][1] < end {
			end = slots2[j][1]
		}
		if end-start >= duration {
			return []int{start, start + duration}
		}
		if slots1[i][1] < slots2[j][1] {
			i++
		} else {
			j++
		}
	}
	return []int{}
}
