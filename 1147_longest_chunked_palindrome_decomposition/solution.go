// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

func longestDecomposition(text string) int {
	n := len(text)
	ans := 0
	i := 0
	for i < n-i {
		found := false
		for length := 1; length <= (n-2*i)/2; length++ {
			if text[i:i+length] == text[n-i-length:n-i] {
				ans += 2
				i += length
				found = true
				break
			}
		}
		if !found {
			ans++
			break
		}
	}
	return ans
}
