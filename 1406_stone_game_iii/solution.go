// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

func stoneGameIII(stoneValue []int) string {
	n := len(stoneValue)
	dp := make([]int, n+1)
	const negInf = int(-1e18)
	for i := n - 1; i >= 0; i-- {
		take := 0
		dp[i] = negInf
		for j := i; j < i+3 && j < n; j++ {
			take += stoneValue[j]
			if take-dp[j+1] > dp[i] {
				dp[i] = take - dp[j+1]
			}
		}
	}
	if dp[0] > 0 {
		return "Alice"
	}
	if dp[0] < 0 {
		return "Bob"
	}
	return "Tie"
}
