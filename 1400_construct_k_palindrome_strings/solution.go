// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

func canConstruct(s string, k int) bool {
	if k > len(s) {
		return false
	}
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
	}
	odd := 0
	for _, v := range count {
		odd += v % 2
	}
	return odd <= k
}
