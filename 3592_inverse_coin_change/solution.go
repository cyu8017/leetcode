// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

func findCoins(numWays []int) []int {
	n := len(numWays)
	// numWays is 1-indexed conceptually but passed as 0-indexed for amounts 1..n
	// LeetCode: numWays[i] is ways for amount i+1? Check stub: numWays []int
	// From problem: 1-indexed array where numWays[i] is ways for amount i.
	// In Go stub typically 0-indexed corresponding to amounts 1..len
	dp := make([]int, n+1)
	dp[0] = 1
	coins := []int{}
	for amt := 1; amt <= n; amt++ {
		ways := 0
		if amt-1 < len(numWays) {
			ways = numWays[amt-1]
		}
		if dp[amt] == ways {
			continue
		}
		if dp[amt]+1 == ways {
			coins = append(coins, amt)
			for x := amt; x <= n; x++ {
				dp[x] += dp[x-amt]
			}
			if dp[amt] != ways {
				return []int{}
			}
			continue
		}
		return []int{}
	}
	return coins
}
