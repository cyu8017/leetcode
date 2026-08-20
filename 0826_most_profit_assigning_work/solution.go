// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

import "sort"

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	type job struct{ d, p int }
	jobs := make([]job, len(difficulty))
	for i := range difficulty {
		jobs[i] = job{difficulty[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i].d < jobs[j].d })
	sort.Ints(worker)
	ans, best, i := 0, 0, 0
	for _, ability := range worker {
		for i < len(jobs) && jobs[i].d <= ability {
			if jobs[i].p > best {
				best = jobs[i].p
			}
			i++
		}
		ans += best
	}
	return ans
}
