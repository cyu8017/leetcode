// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

import "sort"

func maxProfit(workers []int, tasks [][]int) int64 {
	sort.Ints(workers)
	sort.Slice(tasks, func(i, j int) bool { return tasks[i][0] < tasks[j][0] })
	var ans int64
	used := make([]bool, len(tasks))
	for _, w := range workers {
		best, bi := -1, -1
		for i, t := range tasks {
			if used[i] {
				continue
			}
			if t[0] > w {
				break
			}
			if t[1] > best {
				best = t[1]
				bi = i
			}
		}
		if bi >= 0 {
			used[bi] = true
			ans += int64(best)
		}
	}
	// also unpaid tasks? profit is sum of task profits assigned
	return ans
}
