// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

func minInsertions(s string) int {
	insertions, needed := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			needed += 2
			if needed&1 == 1 {
				insertions++
				needed--
			}
		} else {
			needed--
			if needed < 0 {
				insertions++
				needed = 1
			}
		}
	}
	return insertions + needed
}
