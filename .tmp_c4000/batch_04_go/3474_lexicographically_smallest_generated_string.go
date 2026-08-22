// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

func generateString(str1 string, str2 string) string {
	n := len(str1)
	m := len(str2)
	L := n + m - 1
	ans := make([]byte, L)
	for i := range ans {
		ans[i] = '?'
	}
	for i := 0; i < n; i++ {
		if str1[i] == 'T' {
			for j := 0; j < m; j++ {
				if ans[i+j] != '?' && ans[i+j] != str2[j] {
					return ""
				}
				ans[i+j] = str2[j]
			}
		}
	}
	for i := range ans {
		if ans[i] == '?' {
			ans[i] = 'a'
		}
	}
	// fix F constraints
	for i := 0; i < n; i++ {
		if str1[i] == 'F' {
			match := true
			for j := 0; j < m; j++ {
				if ans[i+j] != str2[j] {
					match = false
					break
				}
			}
			if match {
				// need to change a '?' that was set to a - find position we can change
				changed := false
				for j := m - 1; j >= 0; j++ {
					pos := i + j
					// if this pos not forced by any T
					forced := false
					for t := 0; t < n; t++ {
						if str1[t] == 'T' && pos >= t && pos < t+m {
							forced = true
							break
						}
					}
					if !forced {
						ans[pos] = 'b'
						changed = true
						break
					}
				}
				if !changed {
					return ""
				}
			}
		}
	}
	// re-check all
	for i := 0; i < n; i++ {
		match := true
		for j := 0; j < m; j++ {
			if ans[i+j] != str2[j] {
				match = false
				break
			}
		}
		if str1[i] == 'T' && !match {
			return ""
		}
		if str1[i] == 'F' && match {
			return ""
		}
	}
	return string(ans)
}
