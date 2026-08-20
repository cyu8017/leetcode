// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

import "strings"

func crackSafe(n int, k int) string {
	seen := map[string]bool{}
	path := []byte{}
	start := strings.Repeat("0", n-1)
	var dfs func(string)
	dfs = func(node string) {
		for d := 0; d < k; d++ {
			digit := byte('0' + d)
			edge := node + string(digit)
			if !seen[edge] {
				seen[edge] = true
				dfs(edge[1:])
				path = append(path, digit)
			}
		}
	}
	dfs(start)
	return string(path) + start
}
