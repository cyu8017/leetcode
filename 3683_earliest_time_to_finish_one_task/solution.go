// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

func earliestTime(tasks [][]int) int {
	ans := 200
	for _, task := range tasks {
		ans = min(ans, task[0]+task[1])
	}
	return ans
}
