// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

func xorGame(nums []int) bool {
	x := 0
	for _, v := range nums {
		x ^= v
	}
	return x == 0 || len(nums)%2 == 0
}
