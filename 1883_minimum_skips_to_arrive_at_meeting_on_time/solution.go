// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

func minSkips(dist []int, speed int, hoursBefore int) int {
	limit := hoursBefore * speed
	inf := 1 << 62
	dp := make([]int, len(dist)+1)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0

	for _, road := range dist {
		nxt := make([]int, len(dist)+1)
		for i := range nxt {
			nxt[i] = inf
		}
		for skips := 0; skips < len(dist); skips++ {
			if dp[skips] == inf {
				continue
			}
			rest := (dp[skips] + road + speed - 1) / speed * speed
			if rest < nxt[skips] {
				nxt[skips] = rest
			}
			noRest := dp[skips] + road
			if noRest < nxt[skips+1] {
				nxt[skips+1] = noRest
			}
		}
		dp = nxt
	}

	for skips, total := range dp {
		if total <= limit {
			return skips
		}
	}
	return -1
}
