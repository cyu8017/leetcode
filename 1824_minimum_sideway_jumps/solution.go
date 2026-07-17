// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

func minSideJumps(obstacles []int) int {
	const inf = int(1e9)
	dp := [3]int{1, 0, 1}

	for _, obs := range obstacles {
		blocked := [3]bool{obs == 1, obs == 2, obs == 3}
		ndp := [3]int{inf, inf, inf}
		for lane := 0; lane < 3; lane++ {
			if blocked[lane] {
				continue
			}
			for other := 0; other < 3; other++ {
				if blocked[other] || dp[other] == inf {
					continue
				}
				cost := dp[other]
				if lane != other {
					cost++
				}
				if cost < ndp[lane] {
					ndp[lane] = cost
				}
			}
		}
		dp = ndp
	}

	return min(dp[0], min(dp[1], dp[2]))
}
