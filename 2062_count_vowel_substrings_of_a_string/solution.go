// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

func countVowelSubstrings(word string) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	ans := 0
	n := len(word)
	for i := 0; i < n; i++ {
		seen := map[byte]bool{}
		for j := i; j < n && isVowel(word[j]); j++ {
			seen[word[j]] = true
			if len(seen) == 5 {
				ans++
			}
		}
	}
	return ans
}
