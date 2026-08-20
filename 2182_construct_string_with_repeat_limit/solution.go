// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

func repeatLimitedString(s string, repeatLimit int) string {
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	ans := []byte{}
	for {
		placed := false
		for c := 25; c >= 0; c-- {
			if freq[c] == 0 {
				continue
			}
			if len(ans) > 0 && int(ans[len(ans)-1]-'a') == c {
				// need different char
				found := false
				for d := c - 1; d >= 0; d-- {
					if freq[d] > 0 {
						ans = append(ans, byte('a'+d))
						freq[d]--
						found = true
						placed = true
						break
					}
				}
				if !found {
					return string(ans)
				}
				break
			}
			use := freq[c]
			if use > repeatLimit {
				use = repeatLimit
			}
			for i := 0; i < use; i++ {
				ans = append(ans, byte('a'+c))
			}
			freq[c] -= use
			placed = true
			break
		}
		if !placed {
			break
		}
	}
	return string(ans)
}
