// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

func maxCoins(lane1 []int, lane2 []int) int64 {
	n := len(lane1)
	const neg = int64(-1 << 60)
	// dp[i][lane][switched]
	var dp [2][2]int64
	dp[0][0] = int64(lane1[0])
	dp[1][0] = int64(lane2[0])
	dp[0][1], dp[1][1] = neg, neg
	ans := dp[0][0]
	if dp[1][0] > ans {
		ans = dp[1][0]
	}
	for i := 1; i < n; i++ {
		var ndp [2][2]int64
		ndp[0][0] = max64(dp[0][0], 0) + int64(lane1[i])
		ndp[1][0] = max64(dp[1][0], 0) + int64(lane2[i])
		ndp[0][1] = max64(dp[0][1], dp[1][0]) + int64(lane1[i])
		ndp[1][1] = max64(dp[1][1], dp[0][0]) + int64(lane2[i])
		// also start fresh
		if int64(lane1[i]) > ndp[0][0] {
			ndp[0][0] = int64(lane1[i])
		}
		if int64(lane2[i]) > ndp[1][0] {
			ndp[1][0] = int64(lane2[i])
		}
		dp = ndp
		for a := 0; a < 2; a++ {
			for b := 0; b < 2; b++ {
				if dp[a][b] > ans {
					ans = dp[a][b]
				}
			}
		}
	}
	return ans
}

func max64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
