// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

import "sort"

func braceExpansionII(expression string) []string {
	var parse func(expr string, i int) (map[string]bool, int)
	parse = func(expr string, i int) (map[string]bool, int) {
		union := map[string]bool{}
		cur := map[string]bool{"": true}
		for i < len(expr) && expr[i] != '}' {
			if expr[i] == '{' {
				nested, ni := parse(expr, i+1)
				next := map[string]bool{}
				for a := range cur {
					for b := range nested {
						next[a+b] = true
					}
				}
				cur = next
				i = ni
			} else if expr[i] == ',' {
				for k := range cur {
					union[k] = true
				}
				cur = map[string]bool{"": true}
				i++
			} else {
				j := i
				for j < len(expr) && expr[j] >= 'a' && expr[j] <= 'z' {
					j++
				}
				token := expr[i:j]
				next := map[string]bool{}
				for a := range cur {
					next[a+token] = true
				}
				cur = next
				i = j
			}
		}
		for k := range cur {
			union[k] = true
		}
		return union, i + 1
	}
	result, _ := parse(expression, 0)
	ans := make([]string, 0, len(result))
	for k := range result {
		ans = append(ans, k)
	}
	sort.Strings(ans)
	return ans
}
