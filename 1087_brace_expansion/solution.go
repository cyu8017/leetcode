// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

import "sort"

func expand(s string) []string {
	groups := [][]string{}
	i := 0
	for i < len(s) {
		if s[i] == '{' {
			j := i + 1
			for s[j] != '}' {
				j++
			}
			parts := splitComma(s[i+1 : j])
			sort.Strings(parts)
			groups = append(groups, parts)
			i = j + 1
		} else {
			groups = append(groups, []string{string(s[i])})
			i++
		}
	}
	ans := []string{""}
	for _, group := range groups {
		next := make([]string, 0, len(ans)*len(group))
		for _, prefix := range ans {
			for _, ch := range group {
				next = append(next, prefix+ch)
			}
		}
		ans = next
	}
	return ans
}

func splitComma(s string) []string {
	parts := []string{}
	start := 0
	for i := 0; i <= len(s); i++ {
		if i == len(s) || s[i] == ',' {
			parts = append(parts, s[start:i])
			start = i + 1
		}
	}
	return parts
}
