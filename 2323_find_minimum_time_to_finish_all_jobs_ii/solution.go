// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

import "sort"

func minimumTime(jobs []int, workers []int) int {
	sort.Ints(jobs)
	sort.Ints(workers)
	ans := 0
	for i := range jobs {
		days := (jobs[i] + workers[i] - 1) / workers[i]
		if days > ans {
			ans = days
		}
	}
	return ans
}
