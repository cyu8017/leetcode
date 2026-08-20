// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

func leastInterval(tasks []byte, n int) int {
	counts := map[byte]int{}
	maxFreq := 0
	for _, t := range tasks {
		counts[t]++
		if counts[t] > maxFreq {
			maxFreq = counts[t]
		}
	}
	maxCount := 0
	for _, v := range counts {
		if v == maxFreq {
			maxCount++
		}
	}
	candidate := (maxFreq-1)*(n+1) + maxCount
	if len(tasks) > candidate {
		return len(tasks)
	}
	return candidate
}
