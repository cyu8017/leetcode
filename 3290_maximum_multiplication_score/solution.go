// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

func maxScore(a []int, b []int) int64 {
	const neg = int64(-1 << 62)
	dp := [5]int64{0, neg, neg, neg, neg}
	for _, x := range b {
		for k := 4; k >= 1; k-- {
			if dp[k-1] == neg {
				continue
			}
			v := dp[k-1] + int64(a[k-1])*int64(x)
			if v > dp[k] {
				dp[k] = v
			}
		}
	}
	return dp[4]
}
