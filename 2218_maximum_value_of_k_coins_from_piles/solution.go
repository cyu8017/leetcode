// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

func maxValueOfCoins(piles [][]int, k int) int {
	dp := make([]int, k+1)
	for _, pile := range piles {
		ndp := append([]int{}, dp...)
		sum := 0
		for take := 1; take <= len(pile) && take <= k; take++ {
			sum += pile[take-1]
			for j := take; j <= k; j++ {
				if dp[j-take]+sum > ndp[j] {
					ndp[j] = dp[j-take] + sum
				}
			}
		}
		dp = ndp
	}
	return dp[k]
}
