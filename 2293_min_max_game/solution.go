// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

func minMaxGame(nums []int) int {
	for len(nums) > 1 {
		next := make([]int, len(nums)/2)
		for i := 0; i < len(next); i++ {
			if i%2 == 0 {
				if nums[2*i] < nums[2*i+1] {
					next[i] = nums[2*i]
				} else {
					next[i] = nums[2*i+1]
				}
			} else {
				if nums[2*i] > nums[2*i+1] {
					next[i] = nums[2*i]
				} else {
					next[i] = nums[2*i+1]
				}
			}
		}
		nums = next
	}
	return nums[0]
}
