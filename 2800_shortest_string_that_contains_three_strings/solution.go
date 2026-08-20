// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

import "strings"

func minimumString(a string, b string, c string) string {
	merge := func(x, y string) string {
		if strings.Contains(x, y) {
			return x
		}
		best := x + y
		n := len(x)
		if len(y) < n {
			n = len(y)
		}
		for i := n; i > 0; i-- {
			if x[len(x)-i:] == y[:i] {
				cand := x + y[i:]
				if len(cand) < len(best) || (len(cand) == len(best) && cand < best) {
					best = cand
				}
				break
			}
		}
		return best
	}
	perms := [][]string{{a, b, c}, {a, c, b}, {b, a, c}, {b, c, a}, {c, a, b}, {c, b, a}}
	ans := ""
	for _, p := range perms {
		cur := merge(merge(p[0], p[1]), p[2])
		if ans == "" || len(cur) < len(ans) || (len(cur) == len(ans) && cur < ans) {
			ans = cur
		}
	}
	return ans
}
