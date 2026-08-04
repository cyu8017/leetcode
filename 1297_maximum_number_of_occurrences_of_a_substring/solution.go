// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

func maxFreq(s string, maxLetters int, minSize int, maxSize int) int {
	_ = maxSize
	counts := map[string]int{}
	best := 0
	for i := 0; i+minSize <= len(s); i++ {
		sub := s[i : i+minSize]
		seen := map[byte]bool{}
		for j := 0; j < minSize; j++ {
			seen[sub[j]] = true
		}
		if len(seen) <= maxLetters {
			counts[sub]++
			if counts[sub] > best {
				best = counts[sub]
			}
		}
	}
	return best
}
