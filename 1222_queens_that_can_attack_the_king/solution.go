// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	occupied := map[[2]int]bool{}
	for _, q := range queens {
		occupied[[2]int{q[0], q[1]}] = true
	}
	ans := [][]int{}
	for dr := -1; dr <= 1; dr++ {
		for dc := -1; dc <= 1; dc++ {
			if dr == 0 && dc == 0 {
				continue
			}
			r, c := king[0]+dr, king[1]+dc
			for r >= 0 && r < 8 && c >= 0 && c < 8 {
				if occupied[[2]int{r, c}] {
					ans = append(ans, []int{r, c})
					break
				}
				r += dr
				c += dc
			}
		}
	}
	return ans
}
