// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/


import "sort"

func findMinimumTime(tasks [][]int) int {
	sort.Slice(tasks, func(i, j int) bool { return tasks[i][1] < tasks[j][1] })
	used := make([]bool, 2001)
	ans := 0
	for _, t := range tasks {
		start, end, dur := t[0], t[1], t[2]
		have := 0
		for i := start; i <= end; i++ {
			if used[i] {
				have++
			}
		}
		need := dur - have
		for i := end; i >= start && need > 0; i-- {
			if !used[i] {
				used[i] = true
				need--
				ans++
			}
		}
	}
	return ans
}
