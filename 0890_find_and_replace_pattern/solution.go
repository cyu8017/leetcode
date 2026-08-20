// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

func findAndReplacePattern(words []string, pattern string) []string {
	normalize := func(s string) string {
		mapping := map[byte]byte{}
		out := make([]byte, len(s))
		next := byte(0)
		for i := 0; i < len(s); i++ {
			ch := s[i]
			if _, ok := mapping[ch]; !ok {
				mapping[ch] = next
				next++
			}
			out[i] = mapping[ch]
		}
		return string(out)
	}
	target := normalize(pattern)
	ans := []string{}
	for _, w := range words {
		if normalize(w) == target {
			ans = append(ans, w)
		}
	}
	return ans
}
