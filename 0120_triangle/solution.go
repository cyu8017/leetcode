// LeetCode 0120 - Triangle
func minimumTotal(triangle [][]int) int {
	dp := append([]int(nil), triangle[len(triangle)-1]...)
	for i := len(triangle)-2; i >= 0; i-- { for j := 0; j <= i; j++ {
		if dp[j] < dp[j+1] { dp[j] = triangle[i][j] + dp[j] } else { dp[j] = triangle[i][j] + dp[j+1] }
	} }
	return dp[0]
}