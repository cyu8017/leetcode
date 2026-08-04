// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	ans := 0
	for i := range startTime {
		if startTime[i] <= queryTime && queryTime <= endTime[i] {
			ans++
		}
	}
	return ans
}
