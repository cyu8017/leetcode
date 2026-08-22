// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

func lexPalindromicPermutation(s string, target string) string {
	cnt := [26]int{}
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	odd, mid := 0, -1
	for i := 0; i < 26; i++ {
		if cnt[i]%2 == 1 {
			odd++
			mid = i
		}
	}
	if odd > 1 {
		return ""
	}
	half := [26]int{}
	for i := 0; i < 26; i++ {
		half[i] = cnt[i] / 2
	}
	n := len(s)
	halfLen := n / 2
	left := make([]byte, halfLen)
	var dfs func(pos int, greater bool) bool
	dfs = func(pos int, greater bool) bool {
		if pos == halfLen {
			if mid >= 0 {
				if greater {
					return true
				}
				return byte('a'+mid) > target[halfLen]
			}
			return greater
		}
		start := 0
		if !greater {
			start = int(target[pos] - 'a')
		}
		for c := start; c < 26; c++ {
			if half[c] == 0 {
				continue
			}
			half[c]--
			left[pos] = byte('a' + c)
			if dfs(pos+1, greater || c > int(target[pos]-'a')) {
				return true
			}
			half[c]++
		}
		return false
	}
	if !dfs(0, false) {
		return ""
	}
	res := append([]byte{}, left...)
	if mid >= 0 {
		res = append(res, byte('a'+mid))
	}
	for i := halfLen - 1; i >= 0; i-- {
		res = append(res, left[i])
	}
	out := string(res)
	if out <= target {
		return ""
	}
	return out
}
