// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

func findClosestNumber(nums []int) int {
	ans := nums[0]
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for _, x := range nums {
		if abs(x) < abs(ans) || (abs(x) == abs(ans) && x > ans) {
			ans = x
		}
	}
	return ans
}
