// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

func minSessions(tasks []int, sessionTime int) int {
	n := len(tasks)
	type pair struct{ sessions, used int }
	INF := pair{n + 1, 0}
	dp := make([]pair, 1<<n)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = pair{1, 0}
	for mask := 0; mask < 1<<n; mask++ {
		sessions, used := dp[mask].sessions, dp[mask].used
		if sessions > n {
			continue
		}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			t := tasks[i]
			nmask := mask | (1 << i)
			var cand pair
			if used+t <= sessionTime {
				cand = pair{sessions, used + t}
			} else {
				cand = pair{sessions + 1, t}
			}
			if cand.sessions < dp[nmask].sessions || (cand.sessions == dp[nmask].sessions && cand.used < dp[nmask].used) {
				dp[nmask] = cand
			}
		}
	}
	return dp[(1<<n)-1].sessions
}
