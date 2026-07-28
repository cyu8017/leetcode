// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

func camelMatch(queries []string, pattern string) []bool {
	matches := func(q string) bool {
		i := 0
		for j := 0; j < len(q); j++ {
			ch := q[j]
			if i < len(pattern) && ch == pattern[i] {
				i++
			} else if ch >= 'A' && ch <= 'Z' {
				return false
			}
		}
		return i == len(pattern)
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		ans[i] = matches(q)
	}
	return ans
}
