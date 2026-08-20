// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

func constructTransformedArray(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i, x := range nums {
		j := ((i+x)%n + n) % n
		ans[i] = nums[j]
	}
	return ans
}
