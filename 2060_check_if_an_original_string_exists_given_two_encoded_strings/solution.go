// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

func possiblyEquals(s1 string, s2 string) bool {
	n, m := len(s1), len(s2)
	type key struct{ i, j, diff int }
	memo := map[key]bool{}
	var dfs func(i, j, diff int) bool
	dfs = func(i, j, diff int) bool {
		k := key{i, j, diff}
		if v, ok := memo[k]; ok {
			return v
		}
		if i == n && j == m {
			memo[k] = diff == 0
			return memo[k]
		}
		res := false
		if diff == 0 && i < n && j < m && (s1[i] < '0' || s1[i] > '9') && (s2[j] < '0' || s2[j] > '9') {
			if s1[i] == s2[j] {
				res = dfs(i+1, j+1, 0)
			}
		} else if diff > 0 && i < n && (s1[i] < '0' || s1[i] > '9') {
			res = dfs(i+1, j, diff-1)
		} else if diff < 0 && j < m && (s2[j] < '0' || s2[j] > '9') {
			res = dfs(i, j+1, diff+1)
		}
		if !res && i < n && s1[i] >= '0' && s1[i] <= '9' {
			val := 0
			for p := i; p < n && s1[p] >= '0' && s1[p] <= '9'; p++ {
				val = val*10 + int(s1[p]-'0')
				if dfs(p+1, j, diff+val) {
					res = true
					break
				}
			}
		}
		if !res && j < m && s2[j] >= '0' && s2[j] <= '9' {
			val := 0
			for p := j; p < m && s2[p] >= '0' && s2[p] <= '9'; p++ {
				val = val*10 + int(s2[p]-'0')
				if dfs(i, p+1, diff-val) {
					res = true
					break
				}
			}
		}
		memo[k] = res
		return res
	}
	return dfs(0, 0, 0)
}
