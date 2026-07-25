// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

func stoneGameVII(stones []int) int {
	n := len(stones)
	pre := make([]int, n+1)
	for i, x := range stones {
		pre[i+1] = pre[i] + x
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			left := pre[j+1] - pre[i+1] - dp[i+1][j]
			right := pre[j] - pre[i] - dp[i][j-1]
			if left > right {
				dp[i][j] = left
			} else {
				dp[i][j] = right
			}
		}
	}
	return dp[0][n-1]
}
