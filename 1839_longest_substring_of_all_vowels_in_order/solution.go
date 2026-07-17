// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

import "strings"

func longestBeautifulSubstring(word string) int {
	vowels := "aeiou"
	best := 0

	for start := 0; start < len(word); start++ {
		if word[start] != 'a' {
			continue
		}

		counts := [5]int{}
		for end := start; end < len(word); end++ {
			current := word[end]
			if end > start && current < word[end-1] {
				break
			}

			idx := strings.IndexByte(vowels, current)
			counts[idx]++
			if idx > 0 && counts[idx-1] == 0 {
				break
			}
			ok := true
			for _, count := range counts {
				if count == 0 {
					ok = false
					break
				}
			}
			if ok && end-start+1 > best {
				best = end - start + 1
			}
		}
	}
	return best
}
