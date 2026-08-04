// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

func minimumMoves(arr []int) int {
	n := len(arr)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			dp[i][j] = 1 + dp[i+1][j]
			if arr[i] == arr[i+1] {
				v := 1
				if i+2 <= j {
					v += dp[i+2][j]
				}
				if v < dp[i][j] {
					dp[i][j] = v
				}
			}
			for k := i + 2; k <= j; k++ {
				if arr[i] == arr[k] {
					v := dp[i+1][k-1]
					if k < j {
						v += dp[k+1][j]
					}
					if v < dp[i][j] {
						dp[i][j] = v
					}
				}
			}
		}
	}
	return dp[0][n-1]
}
