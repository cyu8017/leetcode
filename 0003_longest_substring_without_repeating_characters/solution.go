// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

func lengthOfLongestSubstring(s string) int {
	last := make(map[byte]int)
	best := 0
	start := 0

	for i := 0; i < len(s); i++ {
		ch := s[i]
		if idx, ok := last[ch]; ok && idx >= start {
			start = idx + 1
		}
		last[ch] = i
		if i-start+1 > best {
			best = i - start + 1
		}
	}

	return best
}
