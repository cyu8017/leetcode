// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

func findMaxK(nums []int) int {
	seen := map[int]bool{}
	ans := -1
	for _, x := range nums {
		seen[x] = true
		if x > 0 && seen[-x] && x > ans {
			ans = x
		}
		if x < 0 && seen[-x] && -x > ans {
			ans = -x
		}
	}
	return ans
}
