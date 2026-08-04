// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import "sort"

func jobScheduling(startTime []int, endTime []int, profit []int) int {
	n := len(startTime)
	jobs := make([][3]int, n)
	for i := 0; i < n; i++ {
		jobs[i] = [3]int{endTime[i], startTime[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i][0] < jobs[j][0] })
	ends := []int{0}
	dp := []int{0}
	for _, job := range jobs {
		end, start, gain := job[0], job[1], job[2]
		i := sort.Search(len(ends), func(i int) bool { return ends[i] > start }) - 1
		best := dp[len(dp)-1]
		if dp[i]+gain > best {
			best = dp[i] + gain
		}
		ends = append(ends, end)
		dp = append(dp, best)
	}
	return dp[len(dp)-1]
}
