// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

import "sort"

func makeLargestSpecial(s string) string {
	parts := []string{}
	balance, start := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			balance++
		} else {
			balance--
		}
		if balance == 0 {
			parts = append(parts, "1"+makeLargestSpecial(s[start+1:i])+"0")
			start = i + 1
		}
	}
	sort.Slice(parts, func(i, j int) bool { return parts[i] > parts[j] })
	out := ""
	for _, p := range parts {
		out += p
	}
	return out
}
