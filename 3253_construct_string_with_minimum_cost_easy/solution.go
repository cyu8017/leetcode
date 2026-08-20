// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

func minimumCost(target string, words []string, costs []int) int {
	const inf = int(1e18)
	n := len(target)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = inf
	}
	best := map[string]int{}
	for i, w := range words {
		if c, ok := best[w]; !ok || costs[i] < c {
			best[w] = costs[i]
		}
	}
	for i := 0; i < n; i++ {
		if dp[i] == inf {
			continue
		}
		for w, c := range best {
			L := len(w)
			if i+L <= n && target[i:i+L] == w && dp[i]+c < dp[i+L] {
				dp[i+L] = dp[i] + c
			}
		}
	}
	if dp[n] == inf {
		return -1
	}
	return dp[n]
}
