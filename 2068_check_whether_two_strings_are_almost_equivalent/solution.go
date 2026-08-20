// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

func checkAlmostEquivalent(word1 string, word2 string) bool {
	freq := [26]int{}
	for i := 0; i < len(word1); i++ {
		freq[word1[i]-'a']++
		freq[word2[i]-'a']--
	}
	for _, v := range freq {
		if v > 3 || v < -3 {
			return false
		}
	}
	return true
}
