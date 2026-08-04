// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

func numKLenSubstrNoRepeats(s string, k int) int {
	if k > len(s) {
		return 0
	}
	window := map[byte]int{}
	for i := 0; i < k; i++ {
		window[s[i]]++
	}
	ans := 0
	if len(window) == k {
		ans = 1
	}
	for i := k; i < len(s); i++ {
		window[s[i]]++
		left := s[i-k]
		window[left]--
		if window[left] == 0 {
			delete(window, left)
		}
		if len(window) == k {
			ans++
		}
	}
	return ans
}
