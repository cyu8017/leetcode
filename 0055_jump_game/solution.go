// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

func canJump(nums []int) bool {
	farthest := 0

	for i, jump := range nums {
		if i > farthest {
			return false
		}
		if i+jump > farthest {
			farthest = i + jump
		}
	}

	return true
}
