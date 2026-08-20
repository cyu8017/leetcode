// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

func waysToSplitArray(nums []int) int {
	var total int64
	for _, v := range nums {
		total += int64(v)
	}
	var left int64
	ans := 0
	for i := 0; i < len(nums)-1; i++ {
		left += int64(nums[i])
		if left >= total-left {
			ans++
		}
	}
	return ans
}
