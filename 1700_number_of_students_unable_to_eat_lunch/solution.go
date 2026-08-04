// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

func countStudents(students []int, sandwiches []int) int {
	count := [2]int{}
	for _, s := range students {
		count[s]++
	}
	for i, x := range sandwiches {
		if count[x] == 0 {
			return len(students) - i
		}
		count[x]--
	}
	return 0
}
