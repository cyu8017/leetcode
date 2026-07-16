// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

func longestSubstring(s string, k int) int {
	if len(s) == 0 {
		return 0
	}

	counts := make(map[byte]int)
	for index := 0; index < len(s); index++ {
		counts[s[index]]++
	}

	for ch, count := range counts {
		if count < k {
			best := 0
			part := make([]byte, 0, len(s))
			for index := 0; index < len(s); index++ {
				if s[index] == ch {
					best = max(best, longestSubstring(string(part), k))
					part = part[:0]
				} else {
					part = append(part, s[index])
				}
			}
			best = max(best, longestSubstring(string(part), k))
			return best
		}
	}

	return len(s)
}
