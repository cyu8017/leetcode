// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

func movesToMakeZigzag(nums []int) int {
	cost := func(start int) int {
		ans := 0
		inf := int(^uint(0) >> 1)
		for i := start; i < len(nums); i += 2 {
			left, right := inf, inf
			if i > 0 {
				left = nums[i-1]
			}
			if i+1 < len(nums) {
				right = nums[i+1]
			}
			limit := left
			if right < limit {
				limit = right
			}
			if nums[i]-limit+1 > 0 {
				ans += nums[i] - limit + 1
			}
		}
		return ans
	}
	a, b := cost(0), cost(1)
	if a < b {
		return a
	}
	return b
}
