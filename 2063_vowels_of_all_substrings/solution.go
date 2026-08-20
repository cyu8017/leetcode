// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

func countVowels(word string) int64 {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	n := len(word)
	var ans int64
	for i := 0; i < n; i++ {
		if isVowel(word[i]) {
			ans += int64(i+1) * int64(n-i)
		}
	}
	return ans
}
