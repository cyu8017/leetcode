// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

func lexGreaterPermutation(s string, target string) string {
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
	}
	n := len(s)
	ans := make([]byte, n)
	var dfs func(pos int, greater bool) bool
	dfs = func(pos int, greater bool) bool {
		if pos == n {
			return greater
		}
		start := 0
		if !greater {
			start = int(target[pos] - 'a')
		}
		for c := start; c < 26; c++ {
			if cnt[c] == 0 {
				continue
			}
			cnt[c]--
			ans[pos] = byte('a' + c)
			ng := greater || c > int(target[pos]-'a')
			if dfs(pos+1, ng) {
				return true
			}
			cnt[c]++
		}
		return false
	}
	if dfs(0, false) {
		return string(ans)
	}
	return ""
}
