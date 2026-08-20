// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/


func isWinner(player1 []int, player2 []int) int {
	score := func(p []int) int {
		s := 0
		for i, x := range p {
			mul := 1
			if (i > 0 && p[i-1] == 10) || (i > 1 && p[i-2] == 10) {
				mul = 2
			}
			s += mul * x
		}
		return s
	}
	a, b := score(player1), score(player2)
	if a > b {
		return 1
	}
	if b > a {
		return 2
	}
	return 0
}
