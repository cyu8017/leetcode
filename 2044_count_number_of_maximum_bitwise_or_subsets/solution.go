// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

func countMaxOrSubsets(nums []int) int {
	maxOr := 0
	for _, x := range nums {
		maxOr |= x
	}
	ans := 0
	var dfs func(i, cur int)
	dfs = func(i, cur int) {
		if i == len(nums) {
			if cur == maxOr {
				ans++
			}
			return
		}
		dfs(i+1, cur)
		dfs(i+1, cur|nums[i])
	}
	dfs(0, 0)
	return ans
}
