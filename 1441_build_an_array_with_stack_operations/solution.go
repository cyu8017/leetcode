// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

func buildArray(target []int, n int) []string {
	answer := []string{}
	current := 1
	for _, value := range target {
		for current < value {
			answer = append(answer, "Push", "Pop")
			current++
		}
		answer = append(answer, "Push")
		current++
	}
	return answer
}
