// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

func shortestSuperstring(s1 string, s2 string) string {
	m, n := len(s1), len(s2)

	if m > n {
		return shortestSuperstring(s2, s1)
	}

	if strings.Contains(s2, s1) {
		return s2
	}

	for i := 0; i < m; i++ {
		if strings.HasPrefix(s2, s1[i:]) {
			return s1[:i] + s2
		}
		if strings.HasSuffix(s2, s1[:m-i]) {
			return s2 + s1[m-i:]
		}
	}

	return s1 + s2
}
