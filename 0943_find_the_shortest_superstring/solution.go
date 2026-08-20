// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

func shortestSuperstring(words []string) string {
	n := len(words)
	overlap := make([][]int, n)
	for i := range overlap {
		overlap[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			a, b := words[i], words[j]
			lim := len(a)
			if len(b) < lim {
				lim = len(b)
			}
			for k := lim; k > 0; k-- {
				if stringsHasSuffixPrefix(a, b, k) {
					overlap[i][j] = k
					break
				}
			}
		}
	}
	dp := make([][]string, 1<<n)
	for i := range dp {
		dp[i] = make([]string, n)
	}
	for i := 0; i < n; i++ {
		dp[1<<i][i] = words[i]
	}
	for mask := 0; mask < 1<<n; mask++ {
		for last := 0; last < n; last++ {
			if mask&(1<<last) == 0 || dp[mask][last] == "" {
				continue
			}
			for nxt := 0; nxt < n; nxt++ {
				if mask&(1<<nxt) != 0 {
					continue
				}
				cand := dp[mask][last] + words[nxt][overlap[last][nxt]:]
				nmask := mask | (1 << nxt)
				if dp[nmask][nxt] == "" || len(cand) < len(dp[nmask][nxt]) {
					dp[nmask][nxt] = cand
				}
			}
		}
	}
	full := (1 << n) - 1
	best := ""
	for _, s := range dp[full] {
		if s != "" && (best == "" || len(s) < len(best)) {
			best = s
		}
	}
	return best
}

func stringsHasSuffixPrefix(a, b string, k int) bool {
	return a[len(a)-k:] == b[:k]
}
