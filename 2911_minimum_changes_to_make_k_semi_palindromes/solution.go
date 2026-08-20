// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

func minimumChanges(s string, k int) int {
	n := len(s)
	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
		for j := range cost[i] {
			cost[i][j] = 1 << 20
		}
	}
	semiCost := func(l, r int) int {
		length := r - l + 1
		best := 1 << 20
		for d := 1; d < length; d++ {
			if length%d != 0 {
				continue
			}
			chg := 0
			for start := 0; start < d; start++ {
				chars := []byte{}
				for i := l + start; i <= r; i += d {
					chars = append(chars, s[i])
				}
				for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
					if chars[i] != chars[j] {
						chg++
					}
				}
			}
			if chg < best {
				best = chg
			}
		}
		return best
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			cost[i][j] = semiCost(i, j)
		}
	}
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = 1 << 20
		}
	}
	dp[0][0] = 0
	for p := 1; p <= k; p++ {
		for i := 1; i <= n; i++ {
			for t := 0; t < i-1; t++ {
				cand := dp[p-1][t] + cost[t][i-1]
				if cand < dp[p][i] {
					dp[p][i] = cand
				}
			}
		}
	}
	return dp[k][n]
}
