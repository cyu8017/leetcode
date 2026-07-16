// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

func minWindow(s string, t string) string {
	if len(t) == 0 {
		return ""
	}

	need := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		need[t[i]]++
	}

	required := len(need)
	formed := 0
	window := make(map[byte]int)
	left := 0
	bestLen := len(s) + 1
	bestLeft := 0

	for right := 0; right < len(s); right++ {
		ch := s[right]
		window[ch]++
		if count, ok := need[ch]; ok && window[ch] == count {
			formed++
		}

		for formed == required {
			if right-left+1 < bestLen {
				bestLen = right - left + 1
				bestLeft = left
			}

			leftCh := s[left]
			window[leftCh]--
			if count, ok := need[leftCh]; ok && window[leftCh] < count {
				formed--
			}
			left++
		}
	}

	if bestLen > len(s) {
		return ""
	}

	return s[bestLeft : bestLeft+bestLen]
}
