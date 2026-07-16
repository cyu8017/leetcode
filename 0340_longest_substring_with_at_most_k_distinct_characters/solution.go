// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

func lengthOfLongestSubstringKDistinct(s string, k int) int {
	if k == 0 {
		return 0
	}

	counts := make(map[byte]int)
	left := 0
	best := 0

	for right := 0; right < len(s); right++ {
		counts[s[right]]++
		for len(counts) > k {
			leftChar := s[left]
			counts[leftChar]--
			if counts[leftChar] == 0 {
				delete(counts, leftChar)
			}
			left++
		}
		if window := right - left + 1; window > best {
			best = window
		}
	}

	return best
}
