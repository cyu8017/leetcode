// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

func characterReplacement(s string, k int) int {
	counts := make(map[byte]int)
	left := 0
	best := 0
	maxCount := 0

	for right := 0; right < len(s); right++ {
		counts[s[right]]++
		if counts[s[right]] > maxCount {
			maxCount = counts[s[right]]
		}
		for (right-left+1)-maxCount > k {
			counts[s[left]]--
			left++
		}
		if right-left+1 > best {
			best = right - left + 1
		}
	}

	return best
}
