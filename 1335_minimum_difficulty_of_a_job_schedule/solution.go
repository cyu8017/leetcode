// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

func minDifficulty(jobDifficulty []int, d int) int {
	n := len(jobDifficulty)
	if n < d {
		return -1
	}
	const inf = int(1e9)
	dp := make([]int, n)
	hardest := 0
	for i, value := range jobDifficulty {
		if value > hardest {
			hardest = value
		}
		dp[i] = hardest
	}
	for day := 1; day < d; day++ {
		nxt := make([]int, n)
		for i := range nxt {
			nxt[i] = inf
		}
		for end := day; end < n; end++ {
			hardest = 0
			for start := end; start >= day; start-- {
				if jobDifficulty[start] > hardest {
					hardest = jobDifficulty[start]
				}
				if dp[start-1]+hardest < nxt[end] {
					nxt[end] = dp[start-1] + hardest
				}
			}
		}
		dp = nxt
	}
	return dp[n-1]
}
