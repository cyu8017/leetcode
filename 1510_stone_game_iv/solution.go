// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

func winnerSquareGame(n int) bool {
	win := make([]bool, n+1)
	for value := 1; value <= n; value++ {
		for root := 1; root*root <= value; root++ {
			if !win[value-root*root] {
				win[value] = true
				break
			}
		}
	}
	return win[n]
}
