// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

func nimGame(piles []int) bool {
	x := 0
	for _, p := range piles {
		x ^= p
	}
	return x != 0
}
