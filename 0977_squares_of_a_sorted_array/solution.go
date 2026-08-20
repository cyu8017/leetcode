// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

func sortedSquares(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	i, j := 0, n-1
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for k := n - 1; k >= 0; k-- {
		if abs(nums[i]) > abs(nums[j]) {
			ans[k] = nums[i] * nums[i]
			i++
		} else {
			ans[k] = nums[j] * nums[j]
			j--
		}
	}
	return ans
}
