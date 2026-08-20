// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

func countPrefixes(words []string, s string) int {
	ans := 0
	for _, w := range words {
		if len(w) <= len(s) && s[:len(w)] == w {
			ans++
		}
	}
	return ans
}
