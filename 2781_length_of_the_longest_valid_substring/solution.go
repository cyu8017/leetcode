// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

func longestValidSubstring(word string, forbidden []string) int {
	forbid := map[string]bool{}
	maxLen := 0
	for _, f := range forbidden {
		forbid[f] = true
		if len(f) > maxLen {
			maxLen = len(f)
		}
	}
	ans := 0
	right := len(word) - 1
	for left := len(word) - 1; left >= 0; left-- {
		for k := left; k <= right && k-left+1 <= maxLen; k++ {
			if forbid[word[left:k+1]] {
				right = k - 1
				break
			}
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
