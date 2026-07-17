// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

func chalkReplacer(chalk []int, k int) int {
	total := 0
	for _, need := range chalk {
		total += need
	}
	k %= total
	for index, need := range chalk {
		if k < need {
			return index
		}
		k -= need
	}
	return 0
}
