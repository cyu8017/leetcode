// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

func hardestWorker(n int, logs [][]int) int {
	ans, best, prev := logs[0][0], logs[0][1], 0
	for _, log := range logs {
		dur := log[1] - prev
		if dur > best || (dur == best && log[0] < ans) {
			best = dur
			ans = log[0]
		}
		prev = log[1]
	}
	return ans
}
