// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

func canPermutePalindrome(s string) bool {
	counts := make([]int, 26)
	for _, char := range s {
		counts[char-'a']++
	}
	odd := 0
	for _, count := range counts {
		if count%2 != 0 {
			odd++
		}
	}
	return odd <= 1
}
