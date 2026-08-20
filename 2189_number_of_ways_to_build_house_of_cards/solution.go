// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

func houseOfCards(n int) int {
	// rows of k triangles use 3k+2? Actually row i uses 2*i + (i-1) = 3*i - 1 cards? 
	// standard: row with k triangles needs 3*k + 2? LeetCode: row i needs 3*i - 1? 
	// walkccc: cards for height h row = 2*h + (h-1) = 3h-1
	dp := make([]int, n+1)
	dp[0] = 1
	for k := 1; 3*k-1 <= n; k++ {
		cost := 3*k - 1
		for j := n; j >= cost; j-- {
			dp[j] += dp[j-cost]
		}
	}
	return dp[n]
}
