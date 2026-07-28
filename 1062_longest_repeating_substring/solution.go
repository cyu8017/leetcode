// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

func longestRepeatingSubstring(s string) int {
	n := len(s)
	hasDup := func(length int) bool {
		seen := map[string]bool{}
		for i := 0; i+length <= n; i++ {
			sub := s[i : i+length]
			if seen[sub] {
				return true
			}
			seen[sub] = true
		}
		return false
	}
	lo, hi, ans := 1, n-1, 0
	for lo <= hi {
		mid := (lo + hi) / 2
		if hasDup(mid) {
			ans = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}
