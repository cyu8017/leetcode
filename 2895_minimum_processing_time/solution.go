// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

import "sort"

func minProcessingTime(processorTime []int, tasks []int) int {
	sort.Ints(processorTime)
	sort.Sort(sort.Reverse(sort.IntSlice(tasks)))
	ans := 0
	for i, p := range processorTime {
		fin := p + tasks[i*4]
		if fin > ans {
			ans = fin
		}
	}
	return ans
}
