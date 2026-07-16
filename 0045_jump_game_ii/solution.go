// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

func jump(nums []int) int {
	jumps := 0
	currentEnd := 0
	farthest := 0

	for i := 0; i < len(nums)-1; i++ {
		if i+nums[i] > farthest {
			farthest = i + nums[i]
		}
		if i == currentEnd {
			jumps++
			currentEnd = farthest
		}
	}

	return jumps
}
