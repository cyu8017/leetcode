// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

func maxScore(n int, k int, stayScore [][]int, travelScore [][]int) int {
	dp := make([]int, n)
	for day := 0; day < k; day++ {
		ndp := make([]int, n)
		for i := range ndp {
			ndp[i] = -1 << 30
		}
		for dest := 0; dest < n; dest++ {
			best := -1 << 30
			for src := 0; src < n; src++ {
				val := dp[src]
				if src == dest {
					val += stayScore[day][dest]
				} else {
					val += travelScore[src][dest]
				}
				if val > best {
					best = val
				}
			}
			ndp[dest] = best
		}
		dp = ndp
	}
	ans := dp[0]
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
