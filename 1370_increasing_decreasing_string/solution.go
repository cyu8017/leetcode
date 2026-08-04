// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

func sortString(s string) string {
	c := [26]int{}
	for i := 0; i < len(s); i++ {
		c[s[i]-'a']++
	}
	out := make([]byte, 0, len(s))
	for len(out) < len(s) {
		for i := 0; i < 26; i++ {
			if c[i] > 0 {
				out = append(out, byte('a'+i))
				c[i]--
			}
		}
		for i := 25; i >= 0; i-- {
			if c[i] > 0 {
				out = append(out, byte('a'+i))
				c[i]--
			}
		}
	}
	return string(out)
}
