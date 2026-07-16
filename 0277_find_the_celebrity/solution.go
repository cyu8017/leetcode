// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

func knows(a, b int) bool {
	return false
}

func findCelebrity(n int) int {
	candidate := 0
	for person := 1; person < n; person++ {
		if knows(candidate, person) {
			candidate = person
		}
	}
	for person := 0; person < n; person++ {
		if person == candidate {
			continue
		}
		if knows(candidate, person) || !knows(person, candidate) {
			return -1
		}
	}
	return candidate
}
