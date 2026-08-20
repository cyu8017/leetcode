// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

func superEggDrop(k int, n int) int {
	dp := make([]int, k+1)
	moves := 0
	for dp[k] < n {
		moves++
		for eggs := k; eggs > 0; eggs-- {
			dp[eggs] = dp[eggs] + dp[eggs-1] + 1
		}
	}
	return moves
}
