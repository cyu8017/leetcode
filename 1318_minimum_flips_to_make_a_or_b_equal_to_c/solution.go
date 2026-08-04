// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

func minFlips(a int, b int, c int) int {
	flips := 0
	for a != 0 || b != 0 || c != 0 {
		x, y, z := a&1, b&1, c&1
		if z == 0 {
			flips += x + y
		} else if x == 0 && y == 0 {
			flips++
		}
		a >>= 1
		b >>= 1
		c >>= 1
	}
	return flips
}
