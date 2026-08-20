// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

func countTexts(pressedKeys string) int {
	const mod = 1000000007
	n := len(pressedKeys)
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1]
		maxPress := 3
		if pressedKeys[i-1] == '7' || pressedKeys[i-1] == '9' {
			maxPress = 4
		}
		for j := 2; j <= maxPress && j <= i; j++ {
			if pressedKeys[i-j] != pressedKeys[i-1] {
				break
			}
			dp[i] = (dp[i] + dp[i-j]) % mod
		}
	}
	return dp[n]
}
