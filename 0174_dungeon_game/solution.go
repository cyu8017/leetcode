// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

func calculateMinimumHP(dungeon [][]int) int {
	rows, cols := len(dungeon), len(dungeon[0])
	dp := make([][]int, rows+1)
	for row := range dp {
		dp[row] = make([]int, cols+1)
		for col := range dp[row] {
			dp[row][col] = 1 << 30
		}
	}
	dp[rows][cols-1], dp[rows-1][cols] = 1, 1

	for row := rows - 1; row >= 0; row-- {
		for col := cols - 1; col >= 0; col-- {
			next := dp[row+1][col]
			if dp[row][col+1] < next {
				next = dp[row][col+1]
			}
			need := next - dungeon[row][col]
			if need < 1 {
				need = 1
			}
			dp[row][col] = need
		}
	}
	return dp[0][0]
}