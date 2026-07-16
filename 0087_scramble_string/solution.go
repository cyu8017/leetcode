// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

func isScramble(s1 string, s2 string) bool {
	memo := make(map[string]bool)

	var dfs func(a, b string) bool
	dfs = func(a, b string) bool {
		key := a + "#" + b
		if v, ok := memo[key]; ok {
			return v
		}
		if a == b {
			memo[key] = true
			return true
		}
		if !sameChars(a, b) {
			memo[key] = false
			return false
		}

		n := len(a)
		for i := 1; i < n; i++ {
			if dfs(a[:i], b[:i]) && dfs(a[i:], b[i:]) {
				memo[key] = true
				return true
			}
			if dfs(a[:i], b[n-i:]) && dfs(a[i:], b[:n-i]) {
				memo[key] = true
				return true
			}
		}
		memo[key] = false
		return false
	}

	return dfs(s1, s2)
}

func sameChars(a, b string) bool {
	if len(a) != len(b) {
		return false
	}
	var count [26]int
	for i := 0; i < len(a); i++ {
		count[a[i]-'a']++
		count[b[i]-'a']--
	}
	for _, c := range count {
		if c != 0 {
			return false
		}
	}
	return true
}
