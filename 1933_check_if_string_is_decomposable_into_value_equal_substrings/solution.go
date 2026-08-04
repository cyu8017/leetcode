// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

func isDecomposable(s string) bool {
	n := len(s)
	i := 0
	twos := 0
	for i < n {
		j := i
		for j < n && s[j] == s[i] {
			j++
		}
		length := j - i
		if length%3 == 1 {
			return false
		}
		if length%3 == 2 {
			twos++
			if twos > 1 {
				return false
			}
		}
		i = j
	}
	return twos == 1
}
