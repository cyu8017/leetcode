// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

func taskSchedulerII(tasks []int, space int) int64 {
	next := map[int]int64{}
	var day int64
	for _, t := range tasks {
		if next[t] > day {
			day = next[t]
		}
		day++
		next[t] = day + int64(space)
	}
	return day
}
