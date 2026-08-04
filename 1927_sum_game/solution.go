// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

func sumGame(num string) bool {
	n := len(num)
	half := n / 2
	score := func(s string) int {
		q, dig := 0, 0
		for i := 0; i < len(s); i++ {
			if s[i] == '?' {
				q++
			} else {
				dig += int(s[i] - '0')
			}
		}
		return dig*2 + q*9
	}
	return score(num[:half]) != score(num[half:])
}
