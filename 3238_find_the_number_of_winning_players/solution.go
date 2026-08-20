// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

func winningPlayerCount(n int, pick [][]int) int {
	cnt := make([][11]int, n)
	s := map[int]struct{}{}
	for _, p := range pick {
		x, y := p[0], p[1]
		cnt[x][y]++
		if cnt[x][y] > x {
			s[x] = struct{}{}
		}
	}
	return len(s)
}
