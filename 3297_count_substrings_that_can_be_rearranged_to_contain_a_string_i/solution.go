// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

func validSubstringCount(word1 string, word2 string) int64 {
	need := [26]int{}
	required := 0
	for _, c := range word2 {
		if need[c-'a'] == 0 {
			required++
		}
		need[c-'a']++
	}
	have := [26]int{}
	formed := 0
	var ans int64
	l := 0
	for r := 0; r < len(word1); r++ {
		c := word1[r] - 'a'
		have[c]++
		if have[c] == need[c] && need[c] > 0 {
			formed++
		}
		for formed == required && l <= r {
			ans += int64(len(word1) - r)
			c2 := word1[l] - 'a'
			if have[c2] == need[c2] && need[c2] > 0 {
				formed--
			}
			have[c2]--
			l++
		}
	}
	return ans
}
