// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

import "sort"

func employeeFreeTime(schedule [][][]int) [][]int {
	intervals := [][]int{}
	for _, employee := range schedule {
		for _, item := range employee {
			intervals = append(intervals, []int{item[0], item[1]})
		}
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	merged := [][]int{}
	for _, iv := range intervals {
		if len(merged) == 0 || merged[len(merged)-1][1] < iv[0] {
			merged = append(merged, []int{iv[0], iv[1]})
		} else if iv[1] > merged[len(merged)-1][1] {
			merged[len(merged)-1][1] = iv[1]
		}
	}
	ans := [][]int{}
	for i := 1; i < len(merged); i++ {
		ans = append(ans, []int{merged[i-1][1], merged[i][0]})
	}
	return ans
}
